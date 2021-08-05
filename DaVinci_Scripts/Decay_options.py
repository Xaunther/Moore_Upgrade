import os, sys
sys.path.append(os.getcwd())

from Configurables import LHCbApp
from options.Decay_properties import props

decay_props = props[os.environ["DECAY"]]

#Output
LHCbApp().DDDBtag = decay_props["dddb_tag"]
LHCbApp().CondDBtag = decay_props["conddb_tag"]
LHCbApp().DataType = "Upgrade"
LHCbApp().Simulation = True
#LHCbApp().Lumi = not LHCbApp().Simulation
