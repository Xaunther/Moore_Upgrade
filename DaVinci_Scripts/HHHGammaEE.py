from GaudiConf import IOHelper, reading
from Configurables import (
    ApplicationMgr,
    LHCbApp,
    createODIN,
    HltANNSvc,
)
import json

#Manually add this folder to system path
import os, sys
sys.path.append(os.getcwd())
from DaVinci_Scripts.ntuple_utils import get_ntuples

from options.Decay_properties import props
DECAY = os.environ["DECAY"].split("_Down")[0].split("_Up")[0]
decay_props = props[DECAY]


# Helper functions to be able to read the Hlt2 data
def get_hlt2_unpackers(is_simulation):
    """Configures algorithms for reading HLT2 output.

    This is a temporary measure until support for Run 3 HLT2 output is added to
    an LHCb application.
    """

    reading_algs = ([reading.decoder()] + reading.unpackers() + [createODIN()])
    if is_simulation:
        reading_algs = reading.mc_unpackers() + reading_algs
    return reading_algs


def configure_packed_locations(tck_location):
    """Configures HltANNSvc to know about packed locations used in Moore.

    tck_location (string): Location of json file containing trigger configuration.

    """

    with open(tck_location) as f:
        tck = json.load(f)
        HltANNSvc(PackedObjectLocations={str(k): v for k, v in tck.items()})


############ End of helper Functions ##############

#Line name for files
linename = "HHHGammaEE"
#Input data
IOHelper('ROOT').inputFiles(
    ['output/{0}/{1}_Moore.mdst'.format(os.environ["DECAY"], linename)],
    clear=True)

dtts, seqs = get_ntuples()

#Read TCK
configure_packed_locations("output/{0}/{1}_Moore_tck.json".format(
    os.environ["DECAY"], linename))

#DaVinci configuration. #Use ALL declared dtts!
ApplicationMgr().TopAlg = get_hlt2_unpackers(is_simulation=True) + [
    seq[1] for seq in seqs.items() if "{0}_".format(linename) in seq[0]
] + [dtt[1] for dtt in dtts.items() if "{0}_".format(linename) in dtt[0]]

LHCbApp().TupleFile = 'output/{0}/{1}_Moore.root'.format(
    os.environ["DECAY"], linename)