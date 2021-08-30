from GaudiConf import IOHelper
import os

#Input data
IOHelper('ROOT').inputFiles(
    [
        'output/{0}/{1}_Moore.mdst'.format(
            os.environ["DECAY"],
            os.environ["LINENAME"],
        )
    ],
    clear=True,
)
