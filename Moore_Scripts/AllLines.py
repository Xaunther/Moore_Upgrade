from Moore import options, run_moore
from Moore.tcks import dump_hlt2_configuration
from RecoConf.global_tools import stateProvider_with_simplified_geom
from Hlt2Conf.lines.rd.b_to_hhgamma import btohhgamma_inclusive_line
from Hlt2Conf.lines.rd.b_to_hhgamma_gamma_to_ee import btohhgammaee_inclusive_line
from Hlt2Conf.lines.rd.b_to_hhhgamma import btohhhgamma_inclusive_line
from Hlt2Conf.lines.rd.b_to_hhhgamma_gamma_to_ee import btohhhgammaee_inclusive_line
from RecoConf.reconstruction_objects import reconstruction
import json
from Configurables import HltANNSvc

import os, sys
sys.path.append(os.getcwd())

#Make the script compatible with ganga
try:
    from options.Decay_properties import props
except ImportError:
    from Decay_properties import props
DECAY = os.environ["DECAY"].split("_Down")[0].split("_Up")[0]
decay_props = props[DECAY]


def all_lines():
    standard_line = [
        btohhgamma_inclusive_line(),
        btohhgammaee_inclusive_line(),
        btohhhgamma_inclusive_line(),
        btohhhgammaee_inclusive_line()
    ]
    return standard_line


#Switch true or false
reco_from_file = decay_props["reco_from_file"]

#Line name for files
linename = "AllLines"

options.output_file = "{0}{1}_Moore.mdst".format(os.environ["outfolder"],
                                                 linename)

public_tools = []
if (not reco_from_file):
    public_tools = [stateProvider_with_simplified_geom()]

with reconstruction.bind(from_file=reco_from_file):
    config = run_moore(options, all_lines, public_tools)

#Dump tck info from Moore (needed by Davinci afterwards)
dump_hlt2_configuration(
    config,
    "{0}{1}_Moore_tck.json".format(os.environ["outfolder"], linename),
)
