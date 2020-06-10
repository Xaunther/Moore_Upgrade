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
)
#Small configs to do here
linename = "Hlt2BToHHGamma_Inclusive_Line"
extra_hadron = "ExtraHadron"


# The addTupleTool machinery tries to mutate this in place, so have to make
# sure to copy it whenever we need it
DEFAULT_TUPLE_TOOLS = (
    "TupleToolKinematic",
    "TupleToolPid",
    "TupleToolGeometry",
)
ROOT_IN_TES = "/Event/HLT2"

# The output of the HLT2 line
line_output = AutomaticData("{1}/{0}/Particles".format(linename, ROOT_IN_TES))
# Extra pions
extra_hadrons = AutomaticData("{0}/{1}/Particles".format(linename, extra_hadron))
extra_hadron_sel = CombineSelection(
    extra_hadron+"Sel",
    inputs=[line_output, extra_hadrons],
    DecayDescriptors=[
    "B*+ -> B0 pi+",
    "B*- -> B0 pi-"
    ]
)
extra_hadron_selseq = SelectionSequence(
    extra_hadron_sel.name() + "Seq",
    TopSelection=extra_hadron_sel
)
#DecayTreeTuple for main line
dtt_line = DecayTreeTuple(
    "MyTuple",
    Inputs=[line_output.outputLocation()],
    Decay="B0 -> ^(K*(892)0 -> ^pi+ ^pi-) ^gamma",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_line.ErrorMax = -1
dtt_line.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]

#DecayTreeTuple for ExtraHadron
dtt_extra_hadron = DecayTreeTuple(
    "Tuple"+extra_hadron,
    Inputs=[extra_hadron_selseq],
    Decay="(B*+ -> ^(B0 -> ^(K*(892)0 -> ^pi+ ^pi-) ^gamma) ^pi+) || (B*- -> ^(B0 -> ^(K*(892)0 -> ^pi+ ^pi-) ^gamma) ^pi-)",
    ToolList=list(DEFAULT_TUPLE_TOOLS)
)
dtt_extra_hadron.ErrorMax = -1
dtt_extra_hadron.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]


DaVinci().DataType = "Upgrade"
DaVinci().Simulation = True
DaVinci().Lumi = not DaVinci().Simulation
DaVinci().InputType = "MDST"
DaVinci().RootInTES = ROOT_IN_TES
DaVinci().UserAlgorithms = [extra_hadron_selseq.sequence(), dtt_line, dtt_extra_hadron]
DaVinci().TupleFile = DaVinci().TupleFile + "_HHGamma.root"

@appendPostConfigAction
def hack():
    """Run UnpackParticlesAndVertices on /Event/HLT2."""
    from Configurables import GaudiSequencer
    unpacker = UnpackParticlesAndVertices(
        InputStream=ROOT_IN_TES,
    )
    GaudiSequencer('DaVinciEventInitSeq').Members.append(unpacker)
