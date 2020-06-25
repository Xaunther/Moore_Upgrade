from Configurables import (
    DaVinci,
    DecayTreeTuple,
    UnpackParticlesAndVertices,
)
from Gaudi.Configuration import appendPostConfigAction
from DecayTreeTuple import Configuration
from PhysSelPython.Selections import (
    AutomaticData,
    CombineSelection,
    SelectionSequence,
    MergedSelection,
)

# Small configs to do here
linename = "Hlt2BToHHHGammaEE_Inclusive_Line"
decay = "(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^(gamma -> ^e+ ^e-)) || (B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^(gamma -> ^e+ ^e-))"
output = "HHHGammaEE"
extra_hadron = "ExtraHadron"
extra_Ks0LL = "ExtraKs0LL"
extra_Ks0DD = "ExtraKs0DD"
extra_LambdaLL = "ExtraLambdaLL"
extra_LambdaDD = "ExtraLambdaDD"
extra_gamma = "ExtraGamma"
extra_pi0_merged = "ExtraPi0Merged"
extra_pi0_resolved = "ExtraPi0Resolved"
dtt_list = []

# The addTupleTool machinery tries to mutate this in place, so have to make
# sure to copy it whenever we need it
DEFAULT_TUPLE_TOOLS = (
    "TupleToolKinematic",
    "TupleToolPid",
    "TupleToolGeometry",
    "TupleToolTrackInfo",
    "TupleToolAngles",
    #    "TupleToolRecoStats",
    "TupleToolMCTruth",
    "MCTupleToolKinematic")
ROOT_IN_TES = "/Event/HLT2"

# The output of the HLT2 line
line_output = AutomaticData("{0}/Particles".format(linename))
dtt_line = DecayTreeTuple(
    linename,
    Inputs=[line_output.outputLocation()],
    Decay=decay,
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_line.ErrorMax = -1
dtt_line.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]
dtt_list.append(dtt_line)

# Extra hadron
extra_hadron_output = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_hadron))
dtt_extra_hadron = DecayTreeTuple(
    extra_hadron,
    Inputs=[extra_hadron_output.outputLocation()],
    Decay="(pi+) || (pi-)",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_extra_hadron.ErrorMax = -1
dtt_extra_hadron.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]
dtt_list.append(dtt_extra_hadron)

#Extra Ks0
extra_Ks0LL_output = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_Ks0LL))
extra_Ks0DD_output = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_Ks0DD))
dtt_extra_Ks0 = DecayTreeTuple(
    "ExtraKs0",
    Inputs=[
        extra_Ks0LL_output.outputLocation(),
        extra_Ks0DD_output.outputLocation()
    ],
    Decay="KS0 -> ^pi+ ^pi-",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_extra_Ks0.ErrorMax = -1
dtt_extra_Ks0.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]
dtt_list.append(dtt_extra_Ks0)

#Extra Lambda
extra_LambdaLL_output = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_LambdaLL))
extra_LambdaDD_output = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_LambdaDD))
dtt_extra_Lambda = DecayTreeTuple(
    "ExtraLambda",
    Inputs=[
        extra_LambdaLL_output.outputLocation(),
        extra_LambdaDD_output.outputLocation()
    ],
    Decay="(Lambda0 -> ^p+ ^pi-) || (Lambda~0 -> ^p~- ^pi+)",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_extra_Lambda.ErrorMax = -1
dtt_extra_Lambda.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]
dtt_list.append(dtt_extra_Lambda)

#Extra gamma
extra_gamma_output = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_gamma))
dtt_extra_gamma = DecayTreeTuple(
    "ExtraGamma",
    Inputs=[extra_gamma_output.outputLocation()],
    Decay="gamma",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_extra_gamma.ErrorMax = -1
dtt_extra_gamma.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]
dtt_list.append(dtt_extra_gamma)

#Extra Pi0
extra_Pi0Merged_output = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_pi0_merged))
extra_Pi0Resolved_output = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_pi0_resolved))
dtt_extra_Pi0 = DecayTreeTuple(
    "ExtraPi0",
    Inputs=[
        extra_Pi0Merged_output.outputLocation(),
        extra_Pi0Resolved_output.outputLocation()
    ],
    Decay="pi0",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_extra_Pi0.ErrorMax = -1
dtt_extra_Pi0.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]
dtt_list.append(dtt_extra_Pi0)

DaVinci().RootInTES = ROOT_IN_TES
DaVinci().UserAlgorithms = dtt_list
DaVinci().TupleFile = DaVinci().TupleFile + "_" + output + ".root"


@appendPostConfigAction
def hack():
    """Run UnpackParticlesAndVertices on /Event/HLT2."""
    from Configurables import GaudiSequencer

    unpacker = UnpackParticlesAndVertices(InputStream=ROOT_IN_TES, )
    GaudiSequencer("DaVinciEventInitSeq").Members.append(unpacker)
