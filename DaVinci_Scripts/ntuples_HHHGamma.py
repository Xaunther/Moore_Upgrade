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
extrasel = ""


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
#soft_pions = AutomaticData("Hlt2CharmD0ToKmPip/SoftPions/Particles")
#dstars = CombineSelection(
#    "CombineD0pi",
#    inputs=[kpi_line, soft_pions],
#    DecayDescriptors=[
#    "D*(2010)+ -> D0 pi+",
#    "D*(2010)- -> D0 pi-"
#    ],
#    DaughtersCuts={
#        "pi+": "PT > 250 * MeV"
#    },
#    CombinationCut=(
#    "in_range(0, (AM - AM1 - AM2), 170)"
#    ),
#    MotherCut=(
#    "(VFASPF(VCHI2PDOF) < 10) &"
#    "in_range(0, (M - M1 - M2), 150)"
#    )
#)
#selseq = SelectionSequence(
#    dstars.name() + "Sequence",
#    TopSelection=dstars
#)

dtt_line = DecayTreeTuple(
    "MyTuple",
    Inputs=[line_output.outputLocation()],
    Decay="B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^gamma || B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^gamma",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_line.ErrorMax = -1
#dtt_kpi.addBranches({
#    "D0": "D0 -> K- K+",
#    "D0_h1": "D0 -> ^K- K+",
#    "D0_h2": "D0 -> K- ^K+",
#})
dtt_line.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]

#dtt_kpi_dst = DecayTreeTuple(
#    "TupleDstToD0pi_D0ToKpi",
#    Inputs=[selseq.outputLocation()],
#    Decay="[D*(2010)+ -> ^([D0]cc -> ^K- ^K+) ^pi+]CC",
#    ToolList=list(DEFAULT_TUPLE_TOOLS),
#)
#dtt_kpi_dst.addBranches({
#    "Dst": "[D*(2010)+ -> ([D0]cc -> K- K+) pi+]CC",
#    "Dst_pi": "[D*(2010)+ -> ([D0]cc -> K- K+) ^pi+]CC",
#    "D0": "[D*(2010)+ -> ^([D0]cc -> K- K+) pi+]CC",
#    "D0_h1": "[D*(2010)+ -> ([D0]cc -> ^K- K+) pi+]CC",
#    "D0_h2": "[D*(2010)+ -> ([D0]cc -> K- ^K+) pi+]CC",
#})
#dtt_kpi_dst.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]

DaVinci().DataType = "Upgrade"
DaVinci().Simulation = True
DaVinci().Lumi = not DaVinci().Simulation
DaVinci().InputType = "MDST"
DaVinci().RootInTES = ROOT_IN_TES
DaVinci().UserAlgorithms = [dtt_line]
DaVinci().TupleFile = DaVinci().TupleFile + "_HHHGamma.root"

@appendPostConfigAction
def hack():
    """Run UnpackParticlesAndVertices on /Event/HLT2."""
    from Configurables import GaudiSequencer
    unpacker = UnpackParticlesAndVertices(
        InputStream=ROOT_IN_TES,
    )
    GaudiSequencer('DaVinciEventInitSeq').Members.append(unpacker)
