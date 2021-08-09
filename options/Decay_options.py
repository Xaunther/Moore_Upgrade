from Moore import options
from Gaudi.Configuration import INFO
import os, sys
sys.path.append(os.getcwd())

from options.Decay_properties import props
decay_props = props[os.environ["DECAY"]]

#Select FT raw bank version. Default is 4, but some samples require version 6
from RecoConf.hlt1_tracking import default_ft_decoding_version
default_ft_decoding_version.global_bind(
    value=decay_props["ft_decoding_version"])

#Define outputfolder here
outfolder = "output/{0}/".format(os.environ["DECAY"])
try:
    os.mkdir(outfolder)
except:
    pass

options.input_type = 'ROOT'
options.input_raw_format = decay_props["input_raw_format"]
options.data_type = 'Upgrade'
options.dddb_tag = decay_props["dddb_tag"]
options.conddb_tag = decay_props["conddb_tag"]
options.simulation = True
options.output_type = 'ROOT'
options.output_level = INFO