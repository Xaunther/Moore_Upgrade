import os
from Configurables import LHCbApp

#Decay name
decname = "OmegaG"
os.environ["DECNAME"] = decname

#Output
LHCbApp().DDDBtag = 'dddb-20171126'
LHCbApp().CondDBtag = 'sim-20171127-vc-md100'
LHCbApp().DataType = "Upgrade"
LHCbApp().Simulation = True
#LHCbApp().Lumi = not LHCbApp().Simulation
