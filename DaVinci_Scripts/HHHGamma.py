import os, sys
sys.path.append(os.getcwd())

from GaudiConf import IOHelper
from Configurables import (
    ApplicationMgr,
    LHCbApp,
)
from Gaudi.Configuration import appendPostConfigAction
from DaVinci_Scripts.ntuple_utils import get_ntuples

#Line name for files
linename = "HHHGamma"
#Input data
IOHelper('ROOT').inputFiles(
    ['output/{0}/{1}_Moore.mdst'.format(os.environ["DECNAME"], linename)],
    clear=True)

dtts, seqs = get_ntuples()

#DaVinci configuration. #Use ALL declared dtts!
ApplicationMgr().TopAlg = [
    seq[1] for seq in seqs.items() if "{0}_".format(linename) in seq[0]
] + [dtt[1] for dtt in dtts.items() if "{0}_".format(linename) in dtt[0]]
LHCbApp().TupleFile = 'output/{0}/{1}_Moore.root'.format(
    os.environ["DECNAME"], linename)


@appendPostConfigAction
def read_hlt2():
    """Configures algorithms for reading HLT2 output.

    This is a temporary measure until support for Run 3 HLT2 output is added to
    an LHCb application.
    """
    import json

    from Configurables import HltANNSvc, createODIN
    from GaudiConf import reading

    # NOTE: You will need to set `raw_event_format` below to 0.3 if:
    # - Your Moore output was MDF or;
    # - Your Moore input was (X)DIGI.
    reading_algs = ([reading.decoder(raw_event_format=4.3)] +
                    reading.unpackers() + [createODIN()])
    if LHCbApp().Simulation:
        reading_algs = reading.mc_unpackers() + reading_algs
    ApplicationMgr().TopAlg = reading_algs + ApplicationMgr().TopAlg

    # Load the 'TCK' dumped from the Moore job
    with open("output/{0}/{1}_Moore_tck.json".format(os.environ["DECNAME"],
                                                     linename)) as f:
        tck = json.load(f)
        HltANNSvc(PackedObjectLocations={str(k): v for k, v in tck.items()})
