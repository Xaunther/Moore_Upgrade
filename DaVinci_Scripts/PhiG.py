#Decay name
decname = "PhiG"

#Input data
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['output/{0}/{0}.dst'.format(decname)], clear=True)

#Output
from Configurables import DaVinci
DaVinci().TupleFile = "output/{0}/{0}".format(decname)
DaVinci().DDDBtag = 'dddb-20171126'
DaVinci().CondDBtag = 'sim-20171127-vc-md100'


