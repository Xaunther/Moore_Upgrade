from Moore import options
from Gaudi.Configuration import INFO
import os, sys
sys.path.append(os.getcwd())

#Make the script compatible with ganga
inganga = False
try:
    from options.Decay_properties import props
except ImportError:
    from Decay_properties import props
    inganga = True
DECAY = os.environ["DECAY"].split("_Down")[0].split("_Up")[0]
decay_props = props[DECAY]

#Whether MagDown or MagUp
if ("Down" in os.environ["DECAY"]):
    mag = "d"
else:
    mag = "u"

#Select FT raw bank version. Default is 4, but some samples require version 6
from RecoConf.hlt1_tracking import default_ft_decoding_version
default_ft_decoding_version.global_bind(
    value=decay_props["ft_decoding_version"])

#Define outputfolder here
if inganga:
    outfolder = "./"
else:
    outfolder = "output/{0}/".format(os.environ["DECAY"])
    try:
        os.mkdir(outfolder)
    except:
        pass
os.environ["outfolder"] = outfolder

options.input_type = 'ROOT'
options.input_raw_format = decay_props["input_raw_format"]
options.data_type = 'Upgrade'
options.dddb_tag = decay_props["dddb_tag"]
options.conddb_tag = decay_props["conddb_tag"].format(mag)
options.simulation = True
options.output_type = 'ROOT'
options.output_level = INFO
