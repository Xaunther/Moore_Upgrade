# Fix for TupleToolGeometry

TupleToolGeometry is unable to recover the list of PVs as it is (2021-08-26). This is a fix in order to be able to recover them both for when using a DaVinci release and the LHCb stack

## DaVinci master flavour

Get DaVinci master release from the nightlies: `lb-dev --platform x86_64_v2-centos7-gcc10-opt --nightly lhcb-master/latest DaVinci/master`. Then, inside DaVinciDev_master folder checkout Phys/DecayTreeTuple folder from Analysis: `git lb-use Analysis && git lb-checkout Analysis/master Phys/DecayTreeTuple`. Finally, copy TupleToolGeometry.cpp into Phys/DecayTreeTuple/src.

## LHCb stack flavour

Then there is the stack version to be used in the stack, where the .h and .cpp have been merged into a single file. Simply copy TupleToolGeometry.cpp into Analysis/Phys/DecayTreeTuple/src folder
