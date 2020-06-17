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
#Small configs to do here
linename = "Hlt2BToHHHGammaEE_Inclusive_Line"
extra_hadron = "ExtraHadron"
extra_Ks0LL = "ExtraKs0LL"
extra_Ks0DD = "ExtraKs0DD"
extra_LambdaLL = "ExtraLambdaLL"
extra_LambdaDD = "ExtraLambdaDD"

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
# Extra selections
extra_hadrons = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_hadron))
extra_Ks0LLs = AutomaticData("{0}/{1}/Particles".format(linename, extra_Ks0LL))
extra_Ks0DDs = AutomaticData("{0}/{1}/Particles".format(linename, extra_Ks0DD))
extra_LambdaLLs = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_LambdaLL))
extra_LambdaDDs = AutomaticData("{0}/{1}/Particles".format(
    linename, extra_LambdaDD))

# Before combining, merge Ks0 and Lambdas
extra_all = MergedSelection("ExtraAllMerged",
                            RequiredSelections=[
                                extra_hadrons, extra_Ks0LLs, extra_Ks0DDs,
                                extra_LambdaLLs, extra_LambdaDDs, extra_Ks0LLs,
                                extra_Ks0DDs
                            ])

# Combinations!
extra_hadron_sel = CombineSelection(
    "ExtraHadronSel",
    inputs=[line_output, extra_all],
    DecayDescriptors=[
        "B*+ -> B+ pi+",
        "B*0 -> B+ pi-",
        "B*0~ -> B- pi+",
        "B*- -> B- pi-",
        "B*+ -> B+ KS0",
        "B*- -> B- KS0",
        "B*+ -> B+ Lambda0",
        "B*+ -> B+ Lambda~0",
        "B*- -> B- Lambda0",
        "B*- -> B- Lambda~0",
    ],
    CombinationCut="APT > 0",
    MotherCut="ALL",
)

#Sequences
extra_hadron_selseq = SelectionSequence(extra_hadron_sel.name() + "Seq",
                                        TopSelection=extra_hadron_sel)

#DecayTreeTuple for main line
dtt_line = DecayTreeTuple(
    linename,
    Inputs=[line_output.outputLocation()],
    Decay=
    "(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^(gamma -> ^e+ ^e-)) || (B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^(gamma -> ^e+ ^e-))",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_line.ErrorMax = -1
dtt_line.addTupleTool("TupleToolANNPID").ANNPIDTunes = ["MC15TuneV1"]

# DecayTreeTuple for ExtraSelection
dtt_line_extra_hadron = DecayTreeTuple(
    linename + "_" + extra_hadron,
    Inputs=[extra_hadron_selseq.outputLocation()],
    Decay=
    """(B*+ -> ^(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^(gamma -> ^e+ ^e-)) ^pi+) ||
             (B*0 -> ^(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^(gamma -> ^e+ ^e-)) ^pi-) ||
             (B*0~ -> ^(B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^(gamma -> ^e+ ^e-)) ^pi+) ||
             (B*- -> ^(B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^(gamma -> ^e+ ^e-)) ^pi-) ||
             (B*+ -> ^(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^(gamma -> ^e+ ^e-)) ^(KS0 -> ^pi+ ^pi-)) ||
             (B*- -> ^(B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^(gamma -> ^e+ ^e-)) ^(KS0 -> ^pi+ ^pi-)) ||
             (B*+ -> ^(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^(gamma -> ^e+ ^e-)) ^(Lambda0 -> ^p+ ^pi-)) ||
             (B*+ -> ^(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^(gamma -> ^e+ ^e-)) ^(Lambda~0 -> ^p~- ^pi+)) ||
             (B*- -> ^(B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^(gamma -> ^e+ ^e-)) ^(Lambda0 -> ^p+ ^pi-)) ||
             (B*- -> ^(B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^(gamma -> ^e+ ^e-)) ^(Lambda~0 -> ^p~- ^pi+))""",
    ToolList=list(DEFAULT_TUPLE_TOOLS),
)
dtt_line_extra_hadron.ErrorMax = -1
dtt_line_extra_hadron.addTupleTool("TupleToolANNPID").ANNPIDTunes = [
    "MC15TuneV1"
]

DaVinci().RootInTES = ROOT_IN_TES
DaVinci().UserAlgorithms = [
    extra_hadron_selseq.sequence(), dtt_line, dtt_line_extra_hadron
]
DaVinci().TupleFile = DaVinci().TupleFile + "_HHHGammaEE.root"


@appendPostConfigAction
def hack():
    """Run UnpackParticlesAndVertices on /Event/HLT2."""
    from Configurables import GaudiSequencer
    unpacker = UnpackParticlesAndVertices(InputStream=ROOT_IN_TES, )
    GaudiSequencer('DaVinciEventInitSeq').Members.append(unpacker)
