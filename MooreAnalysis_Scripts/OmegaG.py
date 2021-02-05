from Moore import options
from Gaudi.Configuration import INFO
import os

#Options for running over data with FT raw bank version 6.
from RecoConf.hlt1_tracking import default_ft_decoding_version
default_ft_decoding_version.global_bind(value=6)

#Decay descriptor to environment
os.environ["DECAY"] = (
    "[${Omega_b}Xi_b- -> (Omega- ->(Lambda0 -> ${pplus}p+ ${piminus}pi-) ${Kminus}K- ) gamma]CC"
)

#Define decay name, will be used around
decname = "OmegaG"
decdesc = "16103332"

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
options.dddb_tag = 'dddb-20190223'
options.conddb_tag = 'sim-20180530-vc-md100'
options.simulation = True
options.ntuple_file = outfolder  #Specify input type in path
options.output_level = INFO