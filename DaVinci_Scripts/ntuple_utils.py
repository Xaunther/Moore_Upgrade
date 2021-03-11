#Script intended to help with ntuple production from MDSTs produced with Moore
from Configurables import DecayTreeTuple
from DecayTreeTuple import Configuration
from PhysSelPython.Selections import AutomaticData, SelectionSequence, CombineSelection
from DecayTreeTuple import DecayTreeTupleTruthUtils

#List of extra LoKi variables to add
LoKi_variables = {"MIPCHI2DV": "MIPCHI2DV(PRIMARY)"}

#MCMatch tools and configurations
relations = [
    "Relations/ChargedPP2MCP",
    "Relations/NeutralPP2MCP",
]
mc_tools = [
    'MCTupleToolKinematic',
    # ...plus any other MC tuple tools you'd like to use
]
mc_tool_list = [
    "TupleToolMCBackgroundInfo",
    "TupleToolMCTruth",
]


#Return list of "simplified" decay descriptors for a given HLT2 + extrasel combination
def get_combo_decaydescriptor(linename, extrasel):
    decaydescriptor = {}
    decaydescriptor["HHGamma_ExtraHadron_Combo"] = [
        "B+ -> B0 pi+",
        "B- -> B0 pi-",
    ]
    return decaydescriptor["{0}_{1}_Combo".format(linename, extrasel)]


#Returns full decay descriptor for a given key
def get_full_decaydescriptor(linename):
    full_decaydescriptor = {}
    full_decaydescriptor["HHGamma"] = "B0 -> ^(K*(892)0 -> ^pi+ ^pi-) ^gamma"
    full_decaydescriptor[
        "HHGammaEE"] = "B0 -> ^(K*(892)0 -> ^pi+ ^pi-) ^(gamma -> ^e+ ^e-)"
    full_decaydescriptor[
        "HHHGamma"] = "(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^gamma) || (B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^gamma)"
    full_decaydescriptor[
        "HHHGammaEE"] = "(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^(gamma -> ^e+ ^e-)) || (B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^(gamma -> ^e+ ^e-))"
    full_decaydescriptor["ExtraHadron"] = "(pi+) || (pi-)"
    full_decaydescriptor["ExtraKs0"] = "KS0 -> ^pi+ ^pi-"
    full_decaydescriptor[
        "ExtraLambda"] = "(Lambda0 -> ^p+ ^pi-) || (Lambda~0 -> ^p~- ^pi+)"
    full_decaydescriptor["ExtraGamma"] = "gamma"
    full_decaydescriptor["ExtraPi0Merged"] = "pi0"
    full_decaydescriptor["ExtraPi0Resolved"] = "pi0 -> ^gamma ^gamma"
    full_decaydescriptor[
        "HHGamma_ExtraHadron_Combo"] = "(B+ -> ^({0}) ^pi+) || (B- -> ^({0}) ^pi-)".format(
            full_decaydescriptor["HHGamma"])
    return full_decaydescriptor[linename]


#Returns branches for a given key
def get_branches(linename):
    branches = {}
    #Branches for HHGamma line
    branches["HHGamma"] = {
        "B": "B0 -> (K*(892)0 -> pi+ pi-) gamma",
        "Kst": "B0 -> ^(K*(892)0 -> pi+ pi-) gamma",
        "piplus": "B0 -> (K*(892)0 -> ^pi+ pi-) gamma",
        "piminus": "B0 -> (K*(892)0 -> pi+ ^pi-) gamma",
        "gamma": "B0 -> (K*(892)0 -> pi+ pi-) ^gamma",
    }
    #Branches for HHGammaEE line
    branches["HHGammaEE"] = {
        "B": "B0 -> (K*(892)0 -> pi+ pi-) (gamma-> e+ e-)",
        "Kst": "B0 -> ^(K*(892)0 -> pi+ pi-) (gamma-> e+ e-)",
        "piplus": "B0 -> (K*(892)0 -> ^pi+ pi-) (gamma-> e+ e-)",
        "piminus": "B0 -> (K*(892)0 -> pi+ ^pi-) (gamma-> e+ e-)",
        "gamma": "B0 -> (K*(892)0 -> pi+ pi-) ^(gamma-> e+ e-)",
        "eplus": "B0 -> (K*(892)0 -> pi+ pi-) (gamma-> ^e+ e-)",
        "eminus": "B0 -> (K*(892)0 -> pi+ pi-) (gamma-> e+ ^e-)",
    }
    #Branches for HHHGamma line
    branches["HHHGamma"] = {
        "B":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) gamma)",
        "Dst":
        "(B+ -> ^(D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) gamma) || (B- -> ^(D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) gamma)",
        "Kst":
        "(B+ -> (D*(2010)+ -> ^(K*(892)0 -> pi+ pi-) pi+) gamma) || (B- -> (D*(2010)- -> ^(K*(892)0 -> pi+ pi-) pi-) gamma)",
        "pi3":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) ^pi+) gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) ^pi-) gamma)",
        "piplus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> ^pi+ pi-) pi+) gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> ^pi+ pi-) pi-) gamma)",
        "piminus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ ^pi-) pi+) gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) ^pi-) gamma)",
        "gamma":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) ^gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) ^gamma)",
    }
    #Branches for HHHGammaEE line
    branches["HHHGammaEE"] = {
        "B":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) (gamma -> e+ e-))",
        "Dst":
        "(B+ -> ^(D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) (gamma -> e+ e-)) || (B- -> ^(D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) (gamma -> e+ e-))",
        "Kst":
        "(B+ -> (D*(2010)+ -> ^(K*(892)0 -> pi+ pi-) pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> ^(K*(892)0 -> pi+ pi-) pi-) (gamma -> e+ e-))",
        "pi3":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) ^pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) ^pi-) (gamma -> e+ e-))",
        "piplus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> ^pi+ pi-) pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> ^pi+ pi-) pi-) (gamma -> e+ e-))",
        "piminus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ ^pi-) pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) ^pi-) (gamma -> e+ e-))",
        "gamma":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) ^(gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) ^(gamma -> e+ e-))",
        "eplus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) (gamma -> ^e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) (gamma -> ^e+ e-))",
        "eminus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) (gamma -> e+ ^e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) (gamma -> e+ ^e-))",
    }
    #Branches for ExtraHadron
    branches["ExtraHadron"] = {"pi": "(pi+) || (pi-)"}
    #Branches for ExtraKs0
    branches["ExtraKs0"] = {
        "Ks0": "KS0 -> pi+ pi-",
        "piplus": "KS0 -> ^pi+ pi-",
        "piminus": "KS0 -> pi+ ^pi-",
    }
    #Branches for ExtraLambda
    branches["ExtraLambda"] = {
        "Lambda": "(Lambda0 -> p+ pi-) || (Lambda~0 -> p~- pi+)",
        "pplus": "(Lambda0 -> ^p+ pi-) || (Lambda~0 -> ^p~- pi+)",
        "piminus": "(Lambda0 -> p+ ^pi-) || (Lambda~0 -> p~- ^pi+)",
    }
    #Branches for ExtraGamma
    branches["ExtraGamma"] = {
        "gamma": "gamma",
    }
    #Branches for ExtraPi0Merged
    branches["ExtraPi0Merged"] = {
        "pi0": "pi0",
    }
    #Branches for ExtraPi0Resolved
    branches["ExtraPi0Resolved"] = {
        "pi0": "pi0 -> gamma gamma",
        "gamma1": "pi0 -> ^gamma gamma",
        "gamma2": "pi0 -> gamma ^gamma",
    }
    return branches[linename]


#Returns AutomaticData instances of the extra selections
#Some require just 1 input, some require 2 (to merge Long and Downstream for example)
def get_extra_inputs_sel(linename, extraname):
    extra_inputs = {}
    #Extra Hadron
    extra_inputs["ExtraHadron"] = [
        AutomaticData(
            "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/ExtraHadron/Particles".
            format(linename)),
    ]
    #Extra Ks0
    extra_inputs["ExtraKs0"] = [
        AutomaticData(
            "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/ExtraKs0LL/Particles".
            format(linename)),
        AutomaticData(
            "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/ExtraKs0DD/Particles".
            format(linename)),
    ]
    #Extra Lambda
    extra_inputs["ExtraLambda"] = [
        AutomaticData(
            "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/ExtraLambdaLL/Particles".
            format(linename)),
        AutomaticData(
            "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/ExtraLambdaDD/Particles".
            format(linename)),
    ]
    #Extra Gamma
    extra_inputs["ExtraGamma"] = [
        AutomaticData(
            "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/ExtraGamma/Particles".
            format(linename)),
    ]
    #Extra Pi0Merged
    extra_inputs["ExtraPi0Merged"] = [
        AutomaticData(
            "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/ExtraPi0Merged/Particles".
            format(linename)),
    ]
    extra_inputs["ExtraPi0Resolved"] = [
        AutomaticData(
            "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/ExtraPi0Resolved/Particles".
            format(linename)),
    ]
    return extra_inputs[extraname]


#Returns array of outputs of the extra selections
#Some require just 1 input, some require 2 (to merge Long and Downstream for example)
def get_extra_inputs(linename, extraname):
    extra_inputs_sel = get_extra_inputs_sel(linename, extraname)
    extra_inputs = [sel.outputLocation() for sel in extra_inputs_sel]
    return extra_inputs


#Returns dictionary with the different extra selections of the radiative lines, combined with a given HLT line
#Needs the name of the HLT2 line and extra selection it combines.
#For now, it will only combine extra hadron with HHGamma (other combinations need further work on the combination, decaydescriptors...)
def get_extra_combined_ntuples(linename, extrasel):
    if (linename != "HHGamma" or extrasel != "ExtraHadron"):
        return {}, {}
    #Inputs
    inputs = get_extra_inputs_sel(linename, extrasel)
    inputs.append(
        AutomaticData("/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/Particles".format(
            linename)))
    #Combine the inputs
    extra_comb = CombineSelection(
        "Combine_HLT2{0}_{1}".format(linename, extrasel),
        inputs=inputs,
        DecayDescriptors=get_combo_decaydescriptor(linename, extrasel),
        CombinationCut=("APT > 0 * GeV"),
        MotherCut=("MIPCHI2DV(PRIMARY) > 0"),
    )
    #Make the sequence
    extra_seq = SelectionSequence(
        extra_comb.name() + "_Sequence", TopSelection=extra_comb)
    #Make the DTT
    dtt = DecayTreeTuple(
        "Tuple_" + extra_comb.name(),
        Inputs=[extra_seq.outputLocation()],
        Decay=get_full_decaydescriptor("{0}_{1}_Combo".format(
            linename, extrasel)),
    )
    #Tupletools
    #MC tools
    dtt.ToolList += mc_tool_list
    DecayTreeTupleTruthUtils.makeTruth(
        dtt, relations, mc_tools, stream="/Event/HLT2")
    #Other tools
    lokitool = dtt.addTupleTool("LoKi::Hybrid::TupleTool/{0}_{1}_Combo".format(
        linename, extrasel))
    lokitool.Variables = LoKi_variables
    #Return dictionary and the sequence
    seq_dict = {"{0}_{1}_Combo".format(linename, extrasel): extra_seq}
    dtt_dict = {"{0}_{1}_Combo".format(linename, extrasel): dtt}
    return dtt_dict, seq_dict


#Returns dictionary with the different extra selections of the radiative lines
#Needs the name of the HLT2 line it is attached to.
def get_extra_ntuples(linename):
    extra_ntuples = {}
    extra_selseqs = {}
    extrasels = [
        "ExtraHadron",
        "ExtraKs0",
        "ExtraLambda",
        "ExtraGamma",
        "ExtraPi0Merged",
        "ExtraPi0Resolved",
    ]
    for extrasel in extrasels:
        ################## LOOP over every extra selection ##################
        extra_ntuples["{0}_{1}".format(linename, extrasel)] = DecayTreeTuple(
            "{0}_{1}Tuple".format(linename, extrasel),
            Inputs=get_extra_inputs(linename, extrasel),
            Decay=get_full_decaydescriptor(extrasel),
        )
        #Branches
        extra_ntuples["{0}_{1}".format(linename, extrasel)].addBranches(
            get_branches(extrasel))
        #Tupletools
        #MC tools
        extra_ntuples["{0}_{1}".format(linename,
                                       extrasel)].ToolList += mc_tool_list
        DecayTreeTupleTruthUtils.makeTruth(
            extra_ntuples["{0}_{1}".format(linename, extrasel)],
            relations,
            mc_tools,
            stream="/Event/HLT2")
        #Other tools
        lokitool = extra_ntuples["{0}_{1}".format(
            linename, extrasel)].addTupleTool(
                "LoKi::Hybrid::TupleTool/{0}_{1}".format(linename, extrasel))
        lokitool.Variables = LoKi_variables
        #Add combination of extra selections with HLT lines
        extra_dtts, extra_seqs = get_extra_combined_ntuples(linename, extrasel)
        extra_ntuples.update(extra_dtts)
        extra_selseqs.update(extra_seqs)
    return extra_ntuples, extra_selseqs


#Returns dictionary with the 4 different dtt configurations
#1 for each inclusive radiative line
def get_ntuples():
    radiative_ntuples = {}
    radiative_seqs = {}
    linenames = [
        "HHGamma",
        "HHGammaEE",
        "HHHGamma",
        "HHHGammaEE",
    ]
    ################## LOOP over every line ##################
    for linename in linenames:
        #Define DTT
        radiative_ntuples[linename] = DecayTreeTuple(
            "{0}Tuple".format(linename),
            Inputs=[
                AutomaticData(
                    "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/Particles".format(
                        linename)).outputLocation()
            ],
            Decay=get_full_decaydescriptor(linename),
        )
        #Branches
        radiative_ntuples[linename].addBranches(get_branches(linename))
        #Tupletools
        #MC tools
        radiative_ntuples[linename].ToolList += mc_tool_list
        DecayTreeTupleTruthUtils.makeTruth(
            radiative_ntuples[linename],
            relations,
            mc_tools,
            stream="/Event/HLT2")
        #Other tools
        lokitool = radiative_ntuples[linename].addTupleTool(
            "LoKi::Hybrid::TupleTool/{0}".format(linename))
        lokitool.Variables = LoKi_variables
        #Add extra selections
        extra_dtts, extra_seqs = get_extra_ntuples(linename)
        radiative_ntuples.update(extra_dtts)
        radiative_seqs.update(extra_seqs)

    #Return dictionary
    return radiative_ntuples, radiative_seqs