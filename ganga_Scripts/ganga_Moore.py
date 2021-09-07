from options.Decay_properties import props

#Parse input arguments
import argparse

parser = argparse.ArgumentParser(description="Make Moore jobs.")
parser.add_argument(
    'decay',
    choices=[
        "KstG", "PhiG", "K1G", "LambdaG", "XiG", "OmegaG", "PhiKstG",
        "PhiPhiG", "PhiKs0G", "K1G_KPiPi0", "PhiPi0G", "KstIsoG", "LambdaPG",
        "PhiKG", "K1G_Cocktail", "L1520G", "RhoG", "MinBias"
    ],
    help='Decay MC to run over')
parser.add_argument(
    'polarity',
    choices=['Up', 'Down'],
    help='Polarity of data-taking to run over')
parser.add_argument(
    '--moore_path',
    default='../MooreDev_master',
    help="Path to Moore lb-dev build")
parser.add_argument(
    '--build_version',
    default='x86_64_v2-centos7-gcc10-opt',
    help="Build version used")
parser.add_argument(
    '--test', action='store_true', help='Run over one file locally')
args = parser.parse_args()

DECAY = args.decay
POLARITY = args.polarity
MOORE_PATH = args.moore_path
BUILD_VERSION = args.build_version
TEST = args.test

#proxy
#ganga bd_ganga.py
app = GaudiExec()
app.directory = MOORE_PATH
app.useGaudiRun = True
app.run_args = ['env DECAY={0}_{1}'.format(DECAY, POLARITY)]
app.options = [
    'options/Decay_options.py',
    'Moore_Scripts/AllLines.py',
]
if TEST:
    app.options.append('options/100_Evts.py')

#Dataset
dataset = BKQuery(
    path=str(props[DECAY]['dirac-path'].format(POLARITY))).getDataset()

#Configure job
j = Job(application=app)
j.inputfiles = ['options/Decay_properties.py']
j.application.platform = BUILD_VERSION
#j.backend.settings['BannedSites'] = ['LCG.RAL-HEP.uk']
j.name = '{0} MC Upgrade Mag{1}'.format(DECAY, POLARITY)  #CHANGE!!
j.comment = "{0} {1}".format(MOORE_PATH.split("/")[-1],
                             BUILD_VERSION)  #CHANGE!!
if TEST:  #Run just 1 file locally
    j.backend = Local()
    j.inputdata = dataset[:1]
else:
    j.backend = Dirac()
    j.inputdata = dataset

j.splitter = SplitByFiles(filesPerJob=10, ignoremissing=True)
j.outputfiles = [
    DiracFile("*.mdst"),
    LocalFile("*stdout"),
    LocalFile("*.json")
]
j.submit()
