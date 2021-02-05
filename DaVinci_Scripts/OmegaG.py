import os
from Configurables import (
    DaVinci,
    UnpackParticlesAndVertices,
)
from Gaudi.Configuration import appendPostConfigAction
#Decay name
decname = "OmegaG"
os.environ["DECNAME"] = decname

#ROOT IN TES (for MDSTs)
ROOT_IN_TES = "/Event/HLT2"

#Output
DaVinci().TupleFile = "output/{0}/{0}".format(decname)
DaVinci().DDDBtag = 'dddb-20171126'
DaVinci().CondDBtag = 'sim-20171127-vc-md100'
DaVinci().DataType = "Upgrade"
DaVinci().Simulation = True
DaVinci().Lumi = not DaVinci().Simulation
DaVinci().InputType = "MDST"
DaVinci().RootInTES = ROOT_IN_TES


@appendPostConfigAction
def unpack_hlt2():
    """Run UnpackParticlesAndVertices on /Event/HLT2.

    This is a temporary measure until support for Run 3 HLT2 output is added to
    DaVinci.
    """
    from Configurables import GaudiSequencer
    unpacker = UnpackParticlesAndVertices(InputStream=ROOT_IN_TES, )
    GaudiSequencer('DaVinciEventInitSeq').Members.append(unpacker)