#Manually add this folder to system path
import os, sys
sys.path.append(os.getcwd())

from GaudiConf import IOHelper
from Configurables import DaVinci
from DaVinci_Scripts.ntuple_utils import get_ntuples

#Line name for files
linename = "AllLines"
#Input data
IOHelper('ROOT').inputFiles(
    ['output/{0}/{1}_Moore.mdst'.format(os.environ["DECNAME"], linename)],
    clear=True)

dtts, seqs = get_ntuples()
#DaVinci configuration. #Use ALL declared dtts!
DaVinci().UserAlgorithms = seqs.values() + dtts.values()
DaVinci().TupleFile = 'output/{0}/{1}_Moore.root'.format(
    os.environ["DECNAME"], linename)
