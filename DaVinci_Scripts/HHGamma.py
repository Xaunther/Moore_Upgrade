import os, sys
sys.path.append(os.getcwd())

from GaudiConf import IOHelper
from Configurables import DaVinci
from DaVinci_Scripts.ntuple_utils import get_ntuples

#Line name for files
linename = "HHGamma"
#Input data
IOHelper('ROOT').inputFiles(
    ['output/{0}/{1}_Moore.mdst'.format(os.environ["DECNAME"], linename)],
    clear=True)

dtts = get_ntuples()

#DaVinci configuration. #Use ALL declared dtts!
DaVinci().UserAlgorithms = [
    dtt[1] for dtt in dtts.items() if "{0}_".format(linename) in dtt[0]
]
DaVinci().TupleFile = 'output/{0}/{1}_Moore.root'.format(
    os.environ["DECNAME"], linename)
