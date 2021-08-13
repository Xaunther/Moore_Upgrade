import os, sys
sys.path.append(os.getcwd())

from Configurables import LHCbApp
from options.Decay_properties import props
DECAY = os.environ["DECAY"].split("_Down")[0].split("_Up")[0]
decay_props = props[DECAY]

#Whether MagDown or MagUp
if ("Down" in os.environ["DECAY"]):
    mag = "d"
else:
    mag = "u"

#Output
LHCbApp().DDDBtag = decay_props["dddb_tag"]
LHCbApp().CondDBtag = decay_props["conddb_tag"].format(mag)
LHCbApp().DataType = "Upgrade"
LHCbApp().Simulation = True
#LHCbApp().Lumi = not LHCbApp().Simulation
