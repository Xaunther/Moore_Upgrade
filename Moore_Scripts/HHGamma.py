from Moore import options, run_moore
from RecoConf.global_tools import stateProvider_with_simplified_geom
from Hlt2Conf.lines.rd.b_to_hhgamma import btohhgamma_inclusive_line
from RecoConf.reconstruction_objects import reconstruction
import json
from Configurables import HltANNSvc

import os, sys
sys.path.append(os.getcwd())

from options.Decay_properties import props
decay_props = props[os.environ["DECAY"]]


def all_lines():
    standard_line = [btohhgamma_inclusive_line()]
    return standard_line


#Switch true or false
reco_from_file = decay_props["reco_from_file"]

#Line name for files
linename = "HHGamma"

options.output_file = "output/{0}/{1}_Moore.mdst".format(
    os.environ["DECAY"], linename)

public_tools = []
if (not reco_from_file):
    public_tools = [stateProvider_with_simplified_geom()]

with reconstruction.bind(from_file=reco_from_file):
    run_moore(options, all_lines, public_tools)

#Dump tck info from Moore (needed by Davinci afterwards)
with open(
        "output/{0}/{1}_Moore_tck.json".format(os.environ["DECAY"], linename),
        "w") as outfile:
    json.dump(HltANNSvc().PackedObjectLocations, outfile)