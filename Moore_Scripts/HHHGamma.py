from Moore import options, run_moore
from RecoConf.global_tools import stateProvider_with_simplified_geom
from RecoConf.hlt1_tracking import default_ft_decoding_version
from Hlt2Conf.lines.rd.b_to_hhhgamma import btohhhgamma_inclusive_line
from RecoConf.reconstruction_objects import reconstruction


def all_lines():
    standard_line = [btohhhgamma_inclusive_line()]
    return standard_line


#Switch true or false
reco_from_file = False

#Line name for files
linename = "HHHGamma"

options.output_file = options.output_file + linename + "_Moore.mdst"

public_tools = []
if (not reco_from_file):
    default_ft_decoding_version.global_bind(value=2)
    public_tools = [stateProvider_with_simplified_geom()]

with reconstruction.bind(from_file=reco_from_file):
    run_moore(options, all_lines, public_tools)
