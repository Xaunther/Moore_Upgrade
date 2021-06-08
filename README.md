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

- [Loose_extra_cuts_2k](https://gitlab.cern.ch/aalfonso/moore_upgrade/-/tree/Loose_extra_cuts_2k): Loose extraselection cuts. Ran on 2000 events per MC sample.
- [Average_extra_cuts_2k](https://gitlab.cern.ch/aalfonso/moore_upgrade/-/tree/Average_extra_cuts_2k): Average extraselection cuts with maximum 3-4 of each extra particles per event. Ran on 2000 events per MC sample.

## Dependencies

In order to run all the scripts provided, other software must be prepared beforehand. Here are instructions to get everything ready.

### LHCb repositories

First, LHCb software is needed, and the [makefile](makefile) is prepared to run on my own compiled stack (which contains latest changes on master). Follow [lb-stack-setup](https://gitlab.cern.ch/rmatev/lb-stack-setup) to setup your own stack or checkout published versions using `lb-dev`. Then, change the paths at the beginning of the [makefile](makefile). The packages needed are:

- **[Moore](https://gitlab.cern.ch/lhcb/Moore)**: Repository for HLT2 lines.
- **[MooreAnalysis](https://gitlab.cern.ch/lhcb/MooreAnalysis/)**: Helper repository to retrieve efficiencies and/or rates.
- **[DaVinci](https://gitlab.cern.ch/lhcb/DaVinci)**: Repository to produce ntuples from mDSTs.

### aalfonso-Analysis-Tools/root

Personal repository with many root scripts. It is [here](https://gitlab.cern.ch/aalfonso-Analysis-Tools/root) and contains instructions on how to compile it. It is used to retrieve the multiplicity of the extraselections.

## Setup

By default the makefile will assume that the stack and aalfonso-Analysis-Tools/root are under ../stack and ../root. If that is your case, everything is already configured as long as your stack has MooreAnalysis, Moore and DaVinci.

Otherwise, you need to configure the first lines in the [makefile](makefile) to match your installation paths

- `ANALYSIS_TOOLS_ROOT`: Path to [aalfonso-Analysis-Tools/root](https://gitlab.cern.ch/aalfonso-Analysis-Tools/root) folder.
- `STACKDIR` (optional): Path to your stack folder. If you compile your own stack, only configuring this variable should accomodate all three LHCb packages.
- `MOOREANALYSIS`: Path to [MooreAnalysis](https://gitlab.cern.ch/lhcb/MooreAnalysis/) folder.
- `MOORE`: Path to [Moore](https://gitlab.cern.ch/lhcb/Moore) folder.
- `DAVINCI`: Path to [DaVinci](https://gitlab.cern.ch/lhcb/DaVinci) folder.

## Snakemake

You can also use snakemake to run the desired scripts.
