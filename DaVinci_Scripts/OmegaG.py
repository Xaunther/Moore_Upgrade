#Decay name
decname = "OmegaG"

#Input data
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['output/{0}/{0}.mdst'.format(decname)], clear=True)

#Output
from Configurables import DaVinci
DaVinci().TupleFile = "output/{0}/{0}".format(decname)
DaVinci().DDDBtag = 'dddb-20190223'
DaVinci().CondDBtag = 'sim-20180530-vc-md100'
DaVinci().DataType = "Upgrade"
DaVinci().Simulation = True
DaVinci().Lumi = not DaVinci().Simulation
DaVinci().InputType = "MDST"


