from options.Decay_properties import props

#Parse input arguments
import argparse

parser = argparse.ArgumentParser(description="Make DaVinci jobs.")
parser.add_argument('decay',
                    choices=[
                        "KstG", "PhiG", "K1G", "LambdaG", "XiG", "OmegaG",
                        "PhiKstG", "PhiPhiG", "PhiKs0G", "K1G_KPiPi0",
                        "PhiPi0G", "KstIsoG", "LambdaPG", "PhiKG",
                        "K1G_Cocktail", "L1520G", "RhoG", "MinBias"
                    ],
                    help='Decay MC to run over')
parser.add_argument('polarity',
                    choices=['Up', 'Down'],
                    help='Polarity of data-taking to run over')
parser.add_argument('--davinci_path',
                    default='../DaVinciDev_master',
                    help="Path to DaVinci lb-dev build")
parser.add_argument('--build_version',
                    default='x86_64_v2-centos7-gcc10-opt',
                    help="Build version used")
parser.add_argument('--test',
                    action='store_true',
                    help='Run over one file locally')
parser.add_argument(
    '--jobN',
    default='-1',
    help="Use in case you want to retry the failed subjobs in the given job")
args = parser.parse_args()

DECAY = args.decay
POLARITY = args.polarity
DAVINCI_PATH = args.davinci_path
BUILD_VERSION = args.build_version
TEST = args.test
JOBNUMBER = int(args.jobN)


#Function that reads the inputdata of the failed subjobs in a given job and puts it in a dataset
def GetFailedDatasets(jobN):
    dataset = LHCbDataset()

    skip = True
    for sj in jobs[jobN].subjobs.select(status="failed"):
        if skip:
            skip = False
            continue
        dataset.extend(sj.inputdata)
    return dataset


#Function that builds LHCbDataset from a file containing list of input files
def BuildDataset(filename):
    dataset = LHCbDataset()

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        dataset.extend(DiracFile("LFN:" + line.rstrip("\n")))
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
#Each file name is 1 line. We must read and remove trailing newline character, as well as add LFN: prefix
#If a valid job number has been provided
if (JOBNUMBER > 0):
    dataset = GetFailedDatasets(JOBNUMBER)
else:
    dataset = BuildDataset("ganga_Scripts/ganga_Moore_LFNs/{0}_{1}".format(
        DECAY, POLARITY))

#Configure job
j = Job(application=app)
j.inputfiles = [
    'options/Decay_properties.py',
    'DaVinci_Scripts/ntuple_utils.py',
    'DaVinci_Scripts/descriptors.py',
    'DaVinci_Scripts/dtt_inputs.py',
    'ganga_Scripts/ganga_tcks/{0}_{1}/AllLines_Moore_tck.json'.format(
        DECAY, POLARITY),
]
j.application.platform = BUILD_VERSION
#j.backend.settings['BannedSites'] = ['LCG.RAL-HEP.uk']
if (JOBNUMBER > 0):
    j.name = 'Job {2}: {0} MC Upgrade ntuples Mag{1}'.format(
        DECAY, POLARITY, JOBNUMBER)
else:
    j.name = '{0} MC Upgrade ntuples Mag{1}'.format(DECAY, POLARITY)  #CHANGE!!
j.comment = "{0} {1}".format(DAVINCI_PATH.split("/")[-1],
                             BUILD_VERSION)  #CHANGE!!
if TEST:  #Run just 1 file locally
    j.backend = Local()
    j.inputdata = dataset[:1]
else:
    j.backend = Dirac()
    j.inputdata = dataset

filesperjob = 3
if (DECAY == "MinBias"):
    filesperjob = 10
j.splitter = SplitByFiles(filesPerJob=filesperjob, ignoremissing=True)
j.outputfiles = [DiracFile("*.root"), LocalFile("*stdout")]
queues.add(j.submit)
