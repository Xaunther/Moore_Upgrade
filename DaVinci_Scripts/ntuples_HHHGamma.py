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
linename = "Hlt2BToHHHGamma_Inclusive_Line"
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
extra_hadrons = AutomaticData("{2}/{0}/{1}/Particles".format(linename, extra_hadron, ROOT_IN_TES))
#DecayTreeTuple for main line
dtt_line = DecayTreeTuple(
    "MyTuple",
    Inputs=[line_output.outputLocation()],
    Decay="(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^gamma) || (B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^gamma)",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_line.ErrorMax = -1
dtt_line.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]

#DecayTreeTuple for ExtraHadron
dtt_extra_hadron = DecayTreeTuple(
    extra_hadron+"Tuple",
    Inputs=[extra_hadrons.outputLocation()],
    Decay="(pi+) || (pi-)",
    ToolList=list(DEFAULT_TUPLE_TOOLS)
)
dtt_extra_hadron.ErrorMax = -1
dtt_extra_hadron.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]


DaVinci().RootInTES = ROOT_IN_TES
DaVinci().UserAlgorithms = [dtt_line, dtt_extra_hadron]
DaVinci().TupleFile = DaVinci().TupleFile + "_HHHGamma.root"

@appendPostConfigAction
def hack():
    """Run UnpackParticlesAndVertices on /Event/HLT2."""
    from Configurables import GaudiSequencer
    unpacker = UnpackParticlesAndVertices(
        InputStream=ROOT_IN_TES,
    )
    GaudiSequencer('DaVinciEventInitSeq').Members.append(unpacker)
