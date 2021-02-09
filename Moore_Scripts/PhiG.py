from Moore import options
from Gaudi.Configuration import INFO
import os

#Define decay name, will be used around
decname = "PhiG"
decdesc = "13102202"

#Define outputfolder here
outfolder = "output/{0}/".format(decname)
try:
    os.mkdir(outfolder)
except:
    pass

options.input_type = 'ROOT'
options.input_raw_format = 4.3
options.evt_max = 20000
options.print_freq = 250
options.data_type = 'Upgrade'
options.dddb_tag = 'dddb-20171126'
options.conddb_tag = 'sim-20171127-vc-md100'
options.simulation = True
options.output_file = outfolder
options.output_type = 'ROOT'
options.output_level = INFO
