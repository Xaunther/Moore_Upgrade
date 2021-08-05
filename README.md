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

## LHCb repositories

First, LHCb software is needed, and the [makefile](makefile) is prepared to run on my own compiled stack (which contains latest changes on master). Follow [lb-stack-setup](https://gitlab.cern.ch/rmatev/lb-stack-setup) to setup your own stack or checkout published versions using `lb-dev`. Then, change the paths at the beginning of the [makefile](makefile). The packages needed are:

- **[Moore](https://gitlab.cern.ch/lhcb/Moore)**: Repository for HLT2 lines.
- **[MooreAnalysis](https://gitlab.cern.ch/lhcb/MooreAnalysis/)**: Helper repository to retrieve efficiencies and/or rates.
- **[DaVinci](https://gitlab.cern.ch/lhcb/DaVinci)**: Repository to produce ntuples from mDSTs.

## aalfonso-Analysis-Tools/root

Personal repository with many root scripts. It is [here](https://gitlab.cern.ch/aalfonso-Analysis-Tools/root) and contains instructions on how to compile it. It is used to retrieve the multiplicity of the extraselections.

## Setup

Once the packages have been downloaded, you need to configure the first lines in the [makefile](makefile) to match your installation paths (no automation in this part... yet):

- `MOOREANALYSIS`: Path to [MooreAnalysis](https://gitlab.cern.ch/lhcb/MooreAnalysis/) folder.
- `MOORE`: Path to [Moore](https://gitlab.cern.ch/lhcb/Moore) folder.
- `DAVINCI`: Path to [DaVinci](https://gitlab.cern.ch/lhcb/DaVinci) folder.
- `ANALYSIS_TOOLS_ROOT`: Path to [aalfonso-Analysis-Tools/root](https://gitlab.cern.ch/aalfonso-Analysis-Tools/root) folder.
- `UPGRADE_BANDWIDTH_STUDIES`: Path to [Upgrade-bandwidth-studies](https://gitlab.cern.ch/lhcb-HLT/upgrade-bandwidth-studies) folder.
- `STACKDIR` (optional): Path to your stack folder. If you compile your own stack, only configuring this variable should accomodate all three LHCb packages.

## MC cheatsheet

We have prepared scripts to run over many, interesting radiative MC samples. We have given a short key name to each of them, which can be related to its EvtNumber down here:

|     Key      |                                         Event Type                                          | Decay descriptor                                                                       |
| :----------: | :-----------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------- |
|     KstG     | [11102202](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/11102202.py) | {[[B0]nos -> (K*(892)0 -> K+ pi-) gamma]cc, [[B0]os -> (K*(892)~0 -> K- pi+) gamma]cc} |
|     PhiG     | [13102202](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/13102202.py) | [B_s0 -> (phi(1020) -> K+ K-) gamma]cc                                                 |
|     K1G      | [12203224](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/12203224.py) | [ B+ -> (K_1(1270)+ -> (X ->  K+ pi- pi+)) gamma ]cc                                   |
|   LambdaG    | [15102307](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/15102307.py) | [Lambda_b0 -> (Lambda0 -> p+ pi-) gamma]cc                                             |
|     XiG      | [16103330](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/16103330.py) | [Xi_b- -> (Xi- ->(Lambda0 -> p+ pi-) pi-) gamma]cc                                     |
|    OmegaG    | [16103332](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/16103332.py) | [Xi_b- -> (Omega- ->(Lambda0 -> p+ pi-) K- ) gamma]cc                                  |
|   PhiKstG    | [11104202](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/11104202.py) | [B0 -> (phi(1020) -> K+ K-) (K*(892)0 -> K+ pi-) gamma]cc                              |
|   PhiPhiG    | [13104212](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/13104212.py) | [B0s -> (phi(1020) -> K+ K-) (phi(1020) -> K+ K-)  gamma]cc                            |
|   PhiKs0G    | [11104372](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/11104372.py) | [Beauty -> (phi(1020) -> K+ K-) (KS0 -> pi+ pi-)  gamma]cc                             |
| K1G_KpiPi0G  | [11202603](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/11202603.py) | [ B0 -> (K_1(1270)0 -> (X0 ->  K+ pi- pi0)) gamma ]cc                                  |
|   PhiPi0G    | [13102212](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/13102212.py) | [B_s0 -> (phi(1020) -> K+ K-) pi0 gamma]cc                                             |
|   KstIsoG    | [12203303](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/12203303.py) | [B+ -> (K*+ -> (K_S0 -> pi+ pi-) pi+) gamma]cc                                         |
|   LambdaPG   | [12103331](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/12103331.py) | [ B+ -> (anti-Lambda0 -> p~- pi+) p gamma]cc                                           |
|    PhiKG     | [12103202](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/12103202.py) | [B+ -> (phi(1020) -> K+ K-) K+ gamma]cc                                                |
| K1G_Cocktail | [12203271](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/12203271.py) | [ B+ -> (K_1+ -> (X ->  K+ pi- pi+)) gamma ]cc                                         |
|    L1520G    | [15102203](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/15102203.py) | [Lambda_b0 -> (Lambda(1520)0 -> p+ K-) gamma]cc                                        |
|     RhoG     | [11102222](http://lhcbdoc.web.cern.ch/lhcbdoc/decfiles/releases/latest/options/11102222.py) | [B0 -> (rho0 -> pi+ pi-) gamma]cc                                                      |
