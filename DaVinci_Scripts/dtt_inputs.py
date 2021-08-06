#Functions that read the output of the HLT2 lines as input for the DecayTreeTuples

from PhysSelPython.Selections import AutomaticData


#Returns AutomaticData instance of the given HLT2 line
def get_inputs(linename):
    return AutomaticData(
        "/Event/HLT2/Hlt2BTo{0}_Inclusive_Line/Particles".format(linename))


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