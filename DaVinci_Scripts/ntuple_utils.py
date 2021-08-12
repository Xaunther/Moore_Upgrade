#Script intended to help with ntuple production from MDSTs produced with Moore
from Configurables import DecayTreeTuple
from DecayTreeTuple import Configuration
from PhysSelPython.Selections import SelectionSequence, CombineSelection
from DecayTreeTuple import DecayTreeTupleTruthUtils
from DaVinci_Scripts import descriptors, dtt_inputs

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

#List of extra selections
extrasels = [
    "ExtraHadron",
    "ExtraKs0",
    "ExtraLambda",
    "ExtraGamma",
    "ExtraPi0Merged",
    "ExtraPi0Resolved",
]


#Returns dictionary with the different extra selections of the radiative lines, combined with a given HLT line
#Needs the name of the HLT2 line and extra selection it combines.
#For now, it will only combine extra hadron with HHGamma (other combinations need further work on the combination, decaydescriptors...)
def get_extra_combined_ntuples(linename, hadron_comb):
    seq_dict = {}
    dtt_dict = {}
    for extrasel in extrasels:
        #Only combine with extra hadrons, for now
        if (extrasel != "ExtraHadron"):
            continue
        #Inputs
        inputs = dtt_inputs.get_extra_inputs_sel(linename, extrasel)
        inputs.append(dtt_inputs.get_inputs(linename))
        #Combine the inputs. Combination and mother cuts are some dummy cuts to make it work
        extra_comb = CombineSelection(
            "Combine_HLT2{0}_{1}_{2}".format(linename, hadron_comb, extrasel),
            inputs=inputs,
            DecayDescriptors=descriptors.get_combo_decaydescriptor(
                linename, hadron_comb, extrasel),
            CombinationCut=("APT > 0 * GeV"),  #Dummy cut that always holds
            MotherCut=("BPVDIRA() < 2"),  #Dummy cut that always holds
        )
        #Make the sequence
        extra_seq = SelectionSequence(
            extra_comb.name() + "_Sequence", TopSelection=extra_comb)
        #Make the DTT
        dtt = DecayTreeTuple(
            "Tuple_" + extra_comb.name(),
            Inputs=[extra_seq.outputLocation()],
            Decay=descriptors.get_full_decaydescriptor(
                "{0}_{1}_{2}_Combo".format(linename, hadron_comb, extrasel)),
        )
        #Tupletools
        #MC tools
        dtt.ToolList += mc_tool_list
        DecayTreeTupleTruthUtils.makeTruth(
            dtt, relations, mc_tools, stream="/Event/HLT2")
        #Other tools
        lokitool = dtt.addTupleTool(
            "LoKi::Hybrid::TupleTool/{0}_{1}_{2}_Combo".format(
                linename, hadron_comb, extrasel))
        lokitool.Variables = LoKi_variables
        #Return dictionary and the sequence
        seq_dict["{0}_{1}_{2}_Combo".format(linename, hadron_comb,
                                            extrasel)] = extra_seq.sequence()
        dtt_dict["{0}_{1}_{2}_Combo".format(linename, hadron_comb,
                                            extrasel)] = dtt
    return dtt_dict, seq_dict


#Returns dictionary with the different extra selections of the radiative lines
#Needs the name of the HLT2 line it is attached to.
def get_extra_ntuples(linename):
    extra_ntuples = {}
    for extrasel in extrasels:
        ################## LOOP over every extra selection ##################
        extra_ntuples["{0}_{1}".format(linename, extrasel)] = DecayTreeTuple(
            "{0}_{1}Tuple".format(linename, extrasel),
            Inputs=dtt_inputs.get_extra_inputs(linename, extrasel),
            Decay=descriptors.get_full_decaydescriptor(extrasel),
        )
        #Branches
        extra_ntuples["{0}_{1}".format(linename, extrasel)].addBranches(
            descriptors.get_branches(extrasel))
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
    return extra_ntuples


#Returns dictionary with the 4 different dtt configurations
#1 for each inclusive radiative line
def get_ntuples():
    radiative_ntuples = {}
    radiative_seqs = {}
    linenames = [
        ["HHGamma", ["hh", "hKs0", "hL0"]],
        ["HHGammaEE", ["hh", "hKs0", "hL0"]],
        ["HHHGamma", ["hhh", "hhKs0", "hhL0"]],
        ["HHHGammaEE", ["hhh", "hhKs0", "hhL0"]],
    ]
    ################## LOOP over every line ##################
    for linename in linenames:
        for hadron_comb in linename[1]:
            #Define DTT
            radiative_ntuples[linename[0] + "_" +
                              hadron_comb] = DecayTreeTuple(
                                  "{0}_{1}Tuple".format(
                                      linename[0], hadron_comb),
                                  Inputs=[
                                      dtt_inputs.get_inputs(
                                          linename[0]).outputLocation()
                                  ],
                                  Decay=descriptors.get_full_decaydescriptor(
                                      linename[0] + "_" + hadron_comb),
                              )
            #Branches
            radiative_ntuples[linename[0] + "_" + hadron_comb].addBranches(
                descriptors.get_branches(linename[0] + "_" + hadron_comb))
            #Tupletools
            #MC tools
            radiative_ntuples[linename[0] + "_" +
                              hadron_comb].ToolList += mc_tool_list
            DecayTreeTupleTruthUtils.makeTruth(
                radiative_ntuples[linename[0] + "_" + hadron_comb],
                relations,
                mc_tools,
                stream="/Event/HLT2")
            #Other tools
            lokitool = radiative_ntuples[
                linename[0] + "_" + hadron_comb].addTupleTool(
                    "LoKi::Hybrid::TupleTool/{0}_{1}".format(
                        linename[0], hadron_comb))
            lokitool.Variables = LoKi_variables
            #Add combination of extra selections with HLT lines
            extra_dtts, extra_seqs = get_extra_combined_ntuples(
                linename[0], hadron_comb)
            radiative_ntuples.update(extra_dtts)
            radiative_seqs.update(extra_seqs)
        #Add extra selections
        extra_dtts = get_extra_ntuples(linename[0])
        radiative_ntuples.update(extra_dtts)

    #Return dictionary
    return radiative_ntuples, radiative_seqs