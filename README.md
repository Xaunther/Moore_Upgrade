# Radinclusive repository

Repository to contain scripts used to run Moore, MooreAnalysis and DaVinci to obtain HLT2 efficiencies, extraselection multiplicities and event sizes from radiative inclusive HLT2 lines.
The flow is controlled with a makefile. The MCs used are `KstG, PhiG, K1G, LambdaG, XiG, OmegaG`. The main commands are:

- `make all`: Run everything
- `make all_MA`: Run MooreAnalysis part only. This produces matched MCDecayTreeTuples and computes line efficiencies over reconstructible events.
- `make alltuples_MA`: Produce matched ntuples with MooreAnalysis.
- `make all_Moore`: Run Moore+DaVinci part only. This produces mDSTs with Moore and then ntuples with Davinci. Computes extraselection multiplicities and average event sizes in the mDST.
- `make HHGamma_multiplicities`: Compute multiplicities using extraselection from HHGamma line only. Uses all MCs.
- `make HHGammaEE_multiplicities`: Compute multiplicities using extraselection from HHGammaEE line only. Uses all MCs.
- `make HHHGamma_multiplicities`: Compute multiplicities using extraselection from HHHGamma line only. Uses all MCs.
- `make HHHGammaEE_multiplicities`: Compute multiplicities using extraselection from HHHGammaEE line only. Uses all MCs.
- `make allEvtSizes_Moore`: Compute all event sizes. One for each MC
- `make allDSTs_Moore`: Produce all mDSTs using Moore.
- `make alltuples_Moore`: Produce all ntuples with DaVinci.

## Outputs

The outputs are all saved in the output folder. Interesting results are all tagged in the repository so that they can be accessed in the future. The list of previous and a short description is added here.

## Dependencies

In order to run all the scripts provided, other software must be prepared beforehand. Here are instructions to get everything ready.

### LHCb repositories

First, LHCb software is needed, and the [makefile](makefile) is prepared to run on my own compiled stack (which contains latest changes on master). Follow [lb-stack-setup](https://gitlab.cern.ch/rmatev/lb-stack-setup) to setup your own stack or checkout published versions using `lb-dev`. Then, change the paths at the beginning of the [makefile](makefile). The packages needed are:

- **[Moore](https://gitlab.cern.ch/lhcb/Moore)**: Repository for HLT2 lines.
- **[MooreAnalysis](https://gitlab.cern.ch/lhcb/MooreAnalysis/)**: Helper repository to retrieve efficiencies and/or rates.
- **[DaVinci](https://gitlab.cern.ch/lhcb/DaVinci)**: Repository to produce ntuples from mDSTs.

### Upgrade-bandwidth-studies

This repository is needed to get the average event size. The repository is [here](https://gitlab.cern.ch/lhcb-HLT/upgrade-bandwidth-studies) and contains instructions on how to compile it. It was a package first used to test upgrade HLT line in a stripping-like fashion. Now one of its scripts is used to get a nice view of the mDST average event size.

### aalfonso-Analysis-Tools/root

Personal repository with many root scripts. It is [here](https://gitlab.cern.ch/aalfonso-Analysis-Tools/root) and contains instructions on how to compile it. It is used to retrieve the multiplicity of the extraselections.

## Setup

Once the packages have been downloaded, you need to configure the first lines in the [makefile](makefile) to match your installation paths (no automation in this part... yet):

- `MOOREANALYSIS`: Path to [MooreAnalysis](https://gitlab.cern.ch/lhcb/MooreAnalysis/) folder.
- `MOORE`: Path to [Moore](https://gitlab.cern.ch/lhcb/Moore) folder.
- `DAVINCI`: Path to [DaVinci](https://gitlab.cern.ch/lhcb/DaVinci) folder.
- `ANALYSIS_TOOLS_ROOT`: Path to [aalfonso-Analysis-Tools/root](https://gitlab.cern.ch/aalfonso-Analysis-Tools/root) folder.
- `UPGRADE_BANDWIDTH_STUDIES`: Path to [Upgrade-bandwidth-studies](https://gitlab.cern.ch/lhcb-HLT/upgrade-bandwidth-studies) folder.
- `STACKDIR` (optional): Path to your stack folder. If you compile your own stack, only configuring this variable should accomodate all three LHCb packages.
