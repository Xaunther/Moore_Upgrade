from Moore import options
from Gaudi.Configuration import INFO
import os

#Define decay name, will be used around
decname = "LambdaG"
decdesc = "15102307"

#Define outputfolder here
outfolder = "output/{0}/".format(decname)
try:
    os.mkdir(outfolder)
except:
    pass

with open("DSTs/{0}_{1}_MagDown.dir".format(decname, decdesc)) as f:
    options.input_files = f.read().splitlines()
f.close()
options.input_type = 'ROOT'
options.input_raw_format = 4.3
options.evt_max = 2000
options.print_freq = 50
options.data_type = 'Upgrade'
options.dddb_tag = 'dddb-20171126'
options.conddb_tag = 'sim-20171127-vc-md100'
options.simulation = True
options.output_file = outfolder
options.output_type = 'ROOT'
options.output_level = INFO
