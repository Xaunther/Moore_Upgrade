# Fix for BackgroundCategory

BackgroundCategory something recovers a null pointer to mother or daughter. When it does, it catches the error but halts the execution. This fix justs allows for DaVinci to keep running when this situation is encountered (it is rare, but sometimes happens).

## DaVinci master flavour

Get DaVinci master release from the nightlies: `lb-dev --platform x86_64_v2-centos7-gcc10-opt --nightly lhcb-master/latest DaVinci/master`. Then, inside DaVinciDev_master folder checkout Phys/DaVinciMCTools folder from Analysis: `git lb-use Analysis && git lb-checkout Analysis/master Phys/DaVinciMCTools`. Finally, copy BackgroundCategory.cpp into Phys/DaVinciMCTools/src.

## LHCb stack flavour

In this case, simply copy BackgroundCategory.cpp into Analysis/Phys/DaVinciMCTools/src folder in your stack.
