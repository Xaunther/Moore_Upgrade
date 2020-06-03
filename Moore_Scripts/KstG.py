from Moore import options
from Gaudi.Configuration import INFO
import os

#Define outputfolder here
outfolder = "output/KstG/"
try:
    os.mkdir(outfolder)
except:
    pass

with open("DSTs/KstG_11102202_MagDown.dir") as f:
    options.input_files = f.read().splitlines()
f.close()
options.input_type = 'ROOT'
options.input_raw_format = 4.3
options.evt_max = -1
options.print_freq = 10000
options.data_type = 'Upgrade'
options.dddb_tag = 'dddb-20171126'
options.conddb_tag = 'sim-20171127-vc-md100'
options.simulation = True
options.output_file = outfolder+'KstG.ldst'
options.output_type = 'ROOT'
options.output_level = INFO
options.control_flow_file = outfolder+'control_flow.gv'
options.data_flow_file = outfolder+'data_flow.gv'
