from GaudiConf import reading
from Configurables import (
    ApplicationMgr,
    LHCbApp,
    createODIN,
    HltANNSvc,
)
from Gaudi.Configuration import appendPostConfigAction
import json

#Manually add this folder to system path
import os, sys
sys.path.append(os.getcwd())

#Make the script compatible with ganga
inganga = False
try:
    from DaVinci_Scripts.ntuple_utils import get_ntuples
    from options.Decay_properties import props
except ImportError:
    from ntuple_utils import get_ntuples
    from Decay_properties import props
    inganga = True
DECAY = os.environ["DECAY"].split("_Down")[0].split("_Up")[0]
decay_props = props[DECAY]

#Line name for files
linename = "AllLines"
os.environ["LINENAME"] = linename

dtts, seqs = get_ntuples()

#DaVinci configuration. #Use ALL declared dtts!
ApplicationMgr().TopAlg = list(seqs.values()) + list(dtts.values())

#Output ntuple
if inganga:
    LHCbApp().TupleFile = '{0}_Moore.root'.format(linename)
else:
    LHCbApp().TupleFile = 'output/{0}/{1}_Moore.root'.format(
        os.environ["DECAY"], linename)


@appendPostConfigAction
def read_hlt2():
    """Configures algorithms for reading HLT2 output.

    This is a temporary measure until support for Run 3 HLT2 output is added to
    an LHCb application.
    """

    reading_algs = ([reading.decoder()] + reading.unpackers() + [createODIN()])
    if LHCbApp().Simulation:
        reading_algs = reading.mc_unpackers() + reading_algs
    ApplicationMgr().TopAlg = reading_algs + ApplicationMgr().TopAlg

    # Load the 'TCK' dumped from the Moore job
    if inganga:
        tck_file = "{0}_Moore_tck.json".format(linename)
    else:
        tck_file = 'output/{0}/{1}_Moore_tck.json'.format(
            os.environ["DECAY"], linename)
    with open(tck_file) as f:
        tck = json.load(f)
        HltANNSvc(PackedObjectLocations={str(k): v for k, v in tck.items()})
