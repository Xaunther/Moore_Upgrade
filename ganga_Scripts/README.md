# Running on ganga

These instructions include a step-by-step guide in how to run the Moore and DaVinci parts from the workflow in ganga. These has been tested using a master release from the nightlies as of August 30th, 2021.

## Running Moore on ganga

First, we need to setup a master release of Moore from the nightlies (preferrably outside this repository), for example:

```sh
lb-dev --platform x86_64_v2-centos7-gcc10-opt --nightly lhcb-master/latest Moore/master
```

Then, checkout relevant packages you want to modify and compile. In our case, we want to use our local modification of the inclusive radiative lines which **apply no cut on the BDT response**:

```sh
cd MooreDev_master
#Skip this part if no modifications are needed
git lb-use Moore
git lb-checkout Moore/master Hlt/Hlt2Conf
cp -r ${stackdir}/Moore/Hlt/Hlt2Conf/python/Hlt2Conf/lines/rd Hlt/Hlt2Conf/python/Hlt2Conf/lines
#Continue here
make
```

Also, don't forget to have the proxy ready:

```sh
lhcb-proxy-init
```

We're all set now, open ganga while in moore_upgrade folder and run [ganga_Moore.py](ganga_Moore.py) within it, for example for a test run with just 1 input file running locally on KstG MC with MagDown polarity:

```sh
Ganga In [0]: %ganga ganga_Scripts/ganga_Moore.py --test KstG Down
```

There are some other options to configure the job, checkout [ganga_Moore.py](ganga_Moore.py) or use `--help`.

## Retrieving Moore outputs

The Moore scripts produce two outputs that we are interested on: a `.mdst` which is stored in Dirac and `.json` containing the TCK, which is saved locally in your gangadir. Each of these outputs has to be brought in order for the DaVinci step to run properly.

### Retrieving the mdst

The mdst is the only DiracFile saved in each subjob, and so its path can be retrieved using the following ganga command:

```python
#Example with job number 630 and subjob number 1
Ganga In [0]: list(jobs[630].subjobs[1].backend.getOutputDataLFNs().getReplicas().keys())[0]
```

This task has to be done manually, but it can be automatized to produce the list of LFNs for a given job, which must be saved into its corresponding file, following the example, [KstG_Down](ganga_Moore_LFNs/KstG_Down). Now now, this should be enough for unfortunately ganga has a bad time setting up the GUID of these files and they have to be fixed, manually, using the LHCbDirac command `dirac-lhcb-fix-file-guid`. We have prepared a script to do so on demand, simply run:

```sh
#Example for KstG with MagDown polarity
python ganga_Scripts/GUID_fixer.py KstG_Down
```

This script will take a while, as it needs to temporary download, clean up the grid files and reupload each mdst individually.

### Retrieving the tck

The corresponding tck must also be manually saved into its corresponding file, in our example case, [AllLines_Moore_tck.json](ganga_tcks/KstG_Down/AllLines_Moore_tck.json). Since the tck is saved locally, it can be directly copied from any of the subjobs folder:

```sh
#Example with job number 630 (KstG with MagDown polarity) and subjob number 1
cp ${gangadir}/workspace/${USER}/LocalXML/630/1/output/AllLines_Moore_tck.json ganga_Scripts/ganga_tcks/KstG_Down/AllLines_Moore_tck.json
```

When the tck has been retrieved and the LFNs fixed, one can proceed to run DaVinci in ganga.

## Running DaVinci on ganga

Analogously to Moore, we must first get a master release of DaVinci for the nightlies:

```sh
lb-dev --platform x86_64_v2-centos7-gcc10-opt --nightly lhcb-master/latest DaVinci/master
```

We then proceed inside the folder and get the Phys/DecayTreeTuple package from Analysis in order to **fix TupleToolGeometry not finding the PVs in the produced mdst**:

```sh
cd DaVinciDev_master
git lb-use Analysis
git lb-checkout Analysis/master Phys/DecayTreeTuple
cp -r ${moore_upgrade}/PV_fix/TupleToolGeometry.cpp Phys/DecayTreeTuple/src
make
```

Again, don't forget to have the proxy ready:

```sh
lhcb-proxy-init
```

Now we can submit the jobs to ganga, also analogously to Moore. For the case of a test job for KstG with MagDown polarity:

```sh
Ganga In [0]: %ganga ganga_Scripts/ganga_DaVinci.py --test KstG Down
```

The only relevant output in this case is the ntuple `AllLines_Moore.root`, which is saved in the grid.

## Retrieving DaVinci outputs

TODO: Retrieve from a ganga job
