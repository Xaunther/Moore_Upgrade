from Moore import options, run_moore
from Hlt2Conf.lines.inclusive_radiative_b.b_to_hhgamma import btohhgamma_inclusive_line
from Hlt2Conf.lines.inclusive_radiative_b.b_to_hhgamma_gamma_to_ee import btohhgammaee_inclusive_line
from Hlt2Conf.lines.inclusive_radiative_b.b_to_hhhgamma import btohhhgamma_inclusive_line
from Hlt2Conf.lines.inclusive_radiative_b.b_to_hhhgamma_gamma_to_ee import btohhhgammaee_inclusive_line
from GaudiKernel.SystemOfUnits import GeV

def all_lines():
    standard_line = [btohhgamma_inclusive_line(), btohhgammaee_inclusive_line(), btohhhgamma_inclusive_line(), btohhhgammaee_inclusive_line()]
#    with filter_protons.bind(pt_min=4.0 * GeV):
#        modified_line = btohhgamma_inclusive_line()
    return standard_line#, modified_line]

run_moore(options, all_lines)
