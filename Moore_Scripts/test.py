from Moore import options
from Gaudi.Configuration import INFO
import os

#Define decay name, will be used around
decname = "PhiG"
decdesc = "13102202"

#Define outputfolder here
outfolder = "./"

options.input_files=["root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000001_1.ldst"]
options.input_type = 'ROOT'
options.input_raw_format = 4.3
options.evt_max = 100
options.print_freq = 1
options.data_type = 'Upgrade'
options.dddb_tag = 'dddb-20171126'
options.conddb_tag = 'sim-20171127-vc-md100'
options.simulation = True
options.output_file = outfolder+decname+'.mdst'
options.output_type = 'ROOT'
options.output_level = INFO
options.control_flow_file = outfolder+'control_flow.gv'
options.data_flow_file = outfolder+'data_flow.gv'
