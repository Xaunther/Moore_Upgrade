# Instructions to train and apply BDT

The steps and configuration used to train the BDTs for the inclusive radiative lines. The "old" BDTs (more precisely, the ones first uploaded to ParamFiles for the upgrade) have the `_old` suffix.

## Location

TMVA generates the `.xml` BDT weights and `.C` factory files inside [default/weights](default/weights) folder. The name of these files can be softly modified when defining the `TMVA::Factory` instance, for example:

```c++
TMVA::Factory *factory = new TMVA::Factory("myBDT", ...);
```

Defines `myBDT_BDT.weights.xml` and `myBDT_BDT.class.C` inside such folder.

## BDT training

The 2-hadron BDTs have been trained with the only 3 samples that have neutral MC info (only using charged MC info allows for a non-negligible background contribution):

- $B^0\to K^{*0}(892)\gamma$ (`HHGamma(EE)_hhTuple` with `B(Kst)_BKGCAT == 30`)
- $B_s\to\phi\gamma$ (`HHGamma(EE)_hhTuple` with `B(Kst)_BKGCAT == 20`)
- $B^+\to K_1^+\gamma$ (`HHGamma(EE)_hhTuple` with `B(Kst)_BKGCAT == 40`)

Therefore, the 3-hadron BDTs only have one MC as signal proxy:

- $B^+\to K_1^+\gamma$ (`HHGamma(EE)_hhhTuple` with `B(Kst)_BKGCAT == 30`)

The converted photon lines, for some reason, do not make the BKGCAT work for the B candidate, so we simply use the BKGCAT for the Kst.

For the background proxy, we only have the minimum bias, but we use all possible decay tree combinations in each BDT:

- HHGamma(EE) lines: `HHGamma(EE)_hhTuple`, `HHGamma(EE)_hKs0Tuple`, `HHGamma(EE)_hL0Tuple`.
- HHHGamma lines: `HHHGamma(EE)_hhhTuple`, `HHHGamma(EE)_hhKs0Tuple`, `HHHGamma(EE)_hhL0Tuple`, `HHHGamma(EE)_hKs0L0Tuple`, `HHHGamma(EE)_hL0L0Tuple`, `HHHGamma(EE)_hKs0Ks0Tuple`.

Step by step, to train the BDT we first strip away all variables not used in the BDT or in the BKGCAT selection,and apply the following BKGCAT cuts (this can be refined by adding mass cuts on the B, for example, but this will do for now). The list of variables for each BDT is saved in `BDTs/Variables/SavedVariables_<line>.txt`.

| BKGCAT selection           | HHGamma          | HHGammaEE          | HHHGamma         | HHHGammaEE         |
| -------------------------- | ---------------- | ------------------ | ---------------- | ------------------ |
| $B^0\to K^{*0}(892)\gamma$ | `B_BKGCAT == 30` | `Kst_BKGCAT == 30` | N/A              | N/A                |
| $B_s\to\phi\gamma$         | `B_BKGCAT == 20` | `Kst_BKGCAT == 20` | N/A              | N/A                |
| $B^+\to K_1^+\gamma$       | `B_BKGCAT == 40` | `Kst_BKGCAT == 40` | `B_BKGCAT == 30` | `Kst_BKGCAT == 30` |

Next, we train the BDTs using [BDTs/Train_BDT.C](BDTs/Train_BDT.C). The signal proxy is specified from `BDTs/Signal_<line>.txt`, while the background proxy is set in `BDTs/Background_<line>.txt`. The variables used to train the BDT are specified at `BDTs/Variables/BDT_Variables_<line>.txt` while some sanity cuts are defined in `BDTs/Cuts/SanityCuts_<line>.txt` to remove the NaNs. To train the `HHGamma` BDT as an example:

```c++
Train_BDT("BDTs/Signal_HHGamma.txt", "BDTs/Background_HHGamma.txt", "BDTs/Variables/BDT_Variables_HHGamma.txt", "HHGamma", "BDTs/Cuts/SanityCuts_HHGamma.txt")
```

## Checking the BDT response

Once we have trained new BDTs, we can check their performance and compare it with the old ones, this is done with [BDTs/Efficiency_BDT.C](BDTs/Efficiency_BDT.C), which allows to get the number of events that pass different cuts of the BDT_response. The output is dumped into a file of choice. For example, to get the results for HHGamma in signal ([BDTs/Effs/Signal_HHGamma.txt](BDTs/Effs/Signal_HHGamma.txt)):

```c++
Efficiency_BDT("BDTs/Signal_HHGamma.txt", "BDTs/Effs/Signal_HHGamma.txt", "BDTs/Variables/BDT_Variables_HHGamma.txt", "HHGamma", 100)
```

The MinBias sample used contains **2810467** events, but this has a [HLT1 VLoose filter](https://cds.cern.ch/record/2688423/files/LHCb-PUB-2019-013.pdf) applied, the original number of events at 30 MHz is **53993474** (`/MC/Upgrade/30000000/Beam7000GeV-Upgrade-MagDown-Nu7.6-25ns-Pythia8/Sim09c-Up02/Reco-Up01/LDST`). Therefore, to have 100Hz output the number of MinBias events after the BDT must be **180**.

| BDT            | 100 Hz BDT cut | Signal events |
| -------------- | -------------- | ------------- |
| HHGamma        | 0.247525       | 17488         |
| HHGamma old    | 0.366337       | 12113         |
| HHGammaEE      | 0.306931       | 1028          |
| HHGammaEE old  | 0.247525       | 835           |
| HHHGamma       | 0.108911       | 4044          |
| HHHGamma old   | 0.0891089      | 4244          |
| HHHGammaEE     | 0.326733       | 29            |
| HHHGammaEE old | 0.247525       | 81            |
