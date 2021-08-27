from options.Decay_properties import props

#Parse input arguments
import argparse

parser = argparse.ArgumentParser(description="Make DaVinci jobs.")
parser.add_argument(
    'decay',
    choices=[
        "KstG", "PhiG", "K1G", "LambdaG", "XiG", "OmegaG", "PhiKstG",
        "PhiPhiG", "PhiKs0G", "K1G_KPiPi0", "PhiPi0G", "KstIsoG", "LambdaPG",
        "PhiKG", "K1G_Cocktail", "L1520G", "RhoG"
    ],
    help='Decay MC to run over')
parser.add_argument(
    'polarity',
    choices=['Up', 'Down'],
    help='Polarity of data-taking to run over')
parser.add_argument(
    '--davinci_path',
    default='../DaVinciDev_v52r0',
    help="Path to DaVinci lb-dev build")
parser.add_argument(
    '--build_version',
    default='x86_64+avx2+fma-centos7-gcc9-opt',
    help="Build version used")
parser.add_argument(
    '--test', action='store_true', help='Run over one file locally')
args = parser.parse_args()

DECAY = args.decay
POLARITY = args.polarity
DAVINCI_PATH = args._path
BUILD_VERSION = args.build_version
TEST = args.test


#Function that builds LHCbDataset from a file containing list of input files
def BuildDataset(filename):
    dataset = LHCbDataset()

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        dataset.extend(line.rstrip("\n"))
    return dataset


#proxy
#ganga bd_ganga.py
app = GaudiExec()
app.directory = DAVINCI_PATH
app.useGaudiRun = True
app.run_args = ['env DECAY={0}_{1}'.format(DECAY, POLARITY)]
app.options = [
    'DaVinci_Scripts/Decay_options.py',
    'DaVinci_Scripts/AllLines.py',
]

#Dataset
#Just a placeholder, imagine each file name is 1 line. We must read and remove trailing newline character
dataset = BuildDataset("some_input_file_for_a_given_MC.txt")

#Configure job
j = Job(application=app)
j.inputfiles = [
    'options/Decay_properties.py',
    'tckfolder/somedecay/AllLines_Moore_tck.json',
]
j.application.platform = BUILD_VERSION
#j.backend.settings['BannedSites'] = ['LCG.RAL-HEP.uk']
j.name = '{0} MC Upgrade ntuples Mag{1}'.format(DECAY, POLARITY)  #CHANGE!!
j.comment = "{0} {1}".format(DAVINCI_PATH.split("/")[-1],
                             BUILD_VERSION)  #CHANGE!!
if TEST:  #Run just 1 file locally
    j.backend = Local()
    j.inputdata = dataset[:1]
else:
    j.backend = Dirac()
    j.inputdata = dataset

j.splitter = SplitByFiles(filesPerJob=10, ignoremissing=True)
j.outputfiles = [DiracFile("*.root"), LocalFile("*stdout")]
j.submit()
