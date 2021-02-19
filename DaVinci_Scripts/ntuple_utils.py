#Script intended to help with ntuple production from MDSTs produced with Moore
from Configurables import DecayTreeTuple
from DecayTreeTuple import Configuration
from PhysSelPython.Selections import AutomaticData

#List of default tuple tools
DEFAULT_TUPLE_TOOLS = (
    "TupleToolKinematic",
    #"TupleToolPid",
    "TupleToolGeometry",
    "TupleToolTrackInfo",
    "TupleToolAngles",
    "TupleToolRecoStats",
    #"TupleToolMCTruth",
    #"MCTupleToolKinematic",
)

#List of extra LoKi variables to add
LoKi_variables = {"MIPCHI2DV": "MIPCHI2DV(PRIMARY)"}


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
def get_extra_inputs(linename, extraname):
    extra_inputs = {}
    #Extra Hadron
    extra_inputs["ExtraHadron"] = [
        AutomaticData("Hlt2BTo{0}_Inclusive_Line/ExtraHadron/Particles".format(
            linename)).outputLocation(),
    ]
    #Extra Ks0
    extra_inputs["ExtraKs0"] = [
        AutomaticData("Hlt2BTo{0}_Inclusive_Line/ExtraKs0LL/Particles".format(
            linename)).outputLocation(),
        AutomaticData("Hlt2BTo{0}_Inclusive_Line/ExtraKs0DD/Particles".format(
            linename)).outputLocation(),
    ]
    #Extra Lambda
    extra_inputs["ExtraLambda"] = [
        AutomaticData("Hlt2BTo{0}_Inclusive_Line/ExtraLambdaLL/Particles".
                      format(linename)).outputLocation(),
        AutomaticData("Hlt2BTo{0}_Inclusive_Line/ExtraLambdaDD/Particles".
                      format(linename)).outputLocation(),
    ]
    #Extra Gamma
    extra_inputs["ExtraGamma"] = [
        AutomaticData("Hlt2BTo{0}_Inclusive_Line/ExtraGamma/Particles".format(
            linename)).outputLocation(),
    ]
    #Extra Pi0Merged
    extra_inputs["ExtraPi0Merged"] = [
        AutomaticData("Hlt2BTo{0}_Inclusive_Line/ExtraPi0Merged/Particles".
                      format(linename)).outputLocation(),
    ]
    extra_inputs["ExtraPi0Resolved"] = [
        AutomaticData("Hlt2BTo{0}_Inclusive_Line/ExtraPi0Resolved/Particles".
                      format(linename)).outputLocation(),
    ]
    return extra_inputs[extraname]


#Returns dictionary with the different extra selections of the radiative lines
#Needs the name of the HLT2 line it is attached to.
def get_extra_ntuples(linename):
    extra_ntuples = {}
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
            ToolList=list(DEFAULT_TUPLE_TOOLS),
        )
        #Branches
        extra_ntuples["{0}_{1}".format(linename, extrasel)].addBranches(
            get_branches(extrasel))
        #Tupletools
        extra_ntuples["{0}_{1}".format(
            linename,
            extrasel)].addTupleTool("TupleToolANNPID").ANNPIDTunes = [
                "MC15TuneV1"
            ]
        lokitool = extra_ntuples["{0}_{1}".format(
            linename, extrasel)].addTupleTool(
                "LoKi::Hybrid::TupleTool/{0}_{1}".format(linename, extrasel))
        lokitool.Variables = LoKi_variables
    return extra_ntuples


#Returns dictionary with the 4 different dtt configurations
#1 for each inclusive radiative line
def get_ntuples():
    radiative_ntuples = {}
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
                AutomaticData("Hlt2BTo{0}_Inclusive_Line/Particles".format(
                    linename)).outputLocation()
            ],
            Decay=get_full_decaydescriptor(linename),
            ToolList=list(DEFAULT_TUPLE_TOOLS),
        )
        #Branches
        radiative_ntuples[linename].addBranches(get_branches(linename))
        #Tupletools
        radiative_ntuples[linename].addTupleTool(
            "TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]
        lokitool = radiative_ntuples[linename].addTupleTool(
            "LoKi::Hybrid::TupleTool/{0}".format(linename))
        lokitool.Variables = LoKi_variables
        #Add extra selections
        radiative_ntuples.update(get_extra_ntuples(linename))

    #Return dictionary
    return radiative_ntuples