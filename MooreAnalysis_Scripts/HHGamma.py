from Moore import options
from HltEfficiencyChecker.config import run_moore_with_tuples
from RecoConf.global_tools import stateProvider_with_simplified_geom
from RecoConf.hlt1_tracking import default_ft_decoding_version
from Hlt2Conf.lines.rd.b_to_hhgamma import btohhgamma_inclusive_line
from RecoConf.reconstruction_objects import reconstruction
import os, sys
sys.path.append(os.getcwd())

from options.Decay_properties import props
decay_props = props[os.environ["DECAY"]]

#Switch true or false
reco_from_file = decay_props["reco_from_file"]

#Line name for files
linename = "HHGamma"


def make_lines():
    return [btohhgamma_inclusive_line()]


options.lines_maker = make_lines
options.ntuple_file = "output/{0}/{1}_MA.mdst".format(os.environ["DECAY"],
                                                      linename)

public_tools = []
if (not reco_from_file):
    public_tools = [stateProvider_with_simplified_geom()]

with reconstruction.bind(from_file=reco_from_file):
    run_moore_with_tuples(options, False, decay_props["descriptor"],
                          public_tools)
