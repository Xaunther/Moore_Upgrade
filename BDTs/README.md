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

On top of that, the variables used for the BDT are applied some sanity cuts as some of them yield NaN values that MUST BE REMOVED.

| BKGCAT selection           | HHGamma          | HHGammaEE          | HHHGamma         | HHHGammaEE         |
| -------------------------- | ---------------- | ------------------ | ---------------- | ------------------ |
| $B^0\to K^{*0}(892)\gamma$ | `B_BKGCAT == 30` | `Kst_BKGCAT == 30` | N/A              | N/A                |
| $B_s\to\phi\gamma$         | `B_BKGCAT == 20` | `Kst_BKGCAT == 20` | N/A              | N/A                |
| $B^+\to K_1^+\gamma$       | `B_BKGCAT == 40` | `Kst_BKGCAT == 40` | `B_BKGCAT == 30` | `Kst_BKGCAT == 30` |
