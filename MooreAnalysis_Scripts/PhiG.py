from Moore import options
from Gaudi.Configuration import INFO
import os

#Decay descriptor to environment
os.environ["DECAY"] = (
    "[${B_s0}B_s0 -> (phi(1020) -> ${Kplus}K+ ${Kminus}K-) gamma]CC")

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
options.evt_max = 2000
options.print_freq = 50
options.data_type = 'Upgrade'
options.dddb_tag = 'dddb-20171126'
options.conddb_tag = 'sim-20171127-vc-md100'
options.simulation = True
options.ntuple_file = outfolder  #Specify input type in path
options.output_level = INFO