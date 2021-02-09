from Moore import options
from Gaudi.Configuration import INFO
import os

#Options for running over data with FT raw bank version 6.
from RecoConf.hlt1_tracking import default_ft_decoding_version
default_ft_decoding_version.global_bind(value=6)

#Define decay name, will be used around
decname = "XiG"
decdesc = "16103330"

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
options.dddb_tag = 'dddb-20190223'
options.conddb_tag = 'sim-20180530-vc-md100'
options.simulation = True
options.output_file = outfolder
options.output_type = 'ROOT'
options.output_level = INFO
