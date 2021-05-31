from Moore import options
from HltEfficiencyChecker.config import run_moore_with_tuples
from RecoConf.global_tools import stateProvider_with_simplified_geom
from RecoConf.hlt1_tracking import default_ft_decoding_version
from Hlt2Conf.lines.rd.b_to_hhgamma import btohhgamma_inclusive_line
from Hlt2Conf.lines.rd.b_to_hhgamma_gamma_to_ee import btohhgammaee_inclusive_line
from Hlt2Conf.lines.rd.b_to_hhhgamma import btohhhgamma_inclusive_line
from Hlt2Conf.lines.rd.b_to_hhhgamma_gamma_to_ee import btohhhgammaee_inclusive_line
from Hlt2Conf.lines.rd.builders.b_tmva_builder import make_b
from RecoConf.reconstruction_objects import reconstruction
import os

#Switch true or false
reco_from_file = False

#Line name for files
linename = "AllLines"


def make_lines():
    lines_list=[]
    # with make_b.bind(bdt_cut=0.95):
    #     lines_list.append(btohhgamma_inclusive_line())
    lines_list.append(btohhgamma_inclusive_line())
    lines_list.append(btohhgammaee_inclusive_line())
    lines_list.append(btohhhgamma_inclusive_line())
    lines_list.append(btohhhgammaee_inclusive_line())
    return lines_list


options.lines_maker = make_lines
options.ntuple_file = options.ntuple_file + linename + "_MA.root"

public_tools = []
if (not reco_from_file):
    default_ft_decoding_version.global_bind(value=2)
    public_tools = [stateProvider_with_simplified_geom()]

with reconstruction.bind(from_file=reco_from_file):
    run_moore_with_tuples(options, False, os.environ["DECAY"], public_tools)
