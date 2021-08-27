# Fix for TupleToolGeometry

TupleToolGeometry is unable to recover the list of PVs as it is (2021-08-26). This is a fix in order to be able to recover them both for when using a DaVinci release and the LHCb stack

## DaVinci v52r0 flavour

Just copy TupleToolGeometry.cpp (.h) into Phys/DecayTreeTuple/src (folder checked out from Analysis). For some reason v54r0 breaks simply when checking out Phys/DecayTreeTuple (the includes are not being found, I hope they'll fix it).

## stack flavour

Then there is the stack version to be used in the stack, where the .h and .cpp have been merged into a single file. Simply copy TupleToolGeometry.cpp into Analysis/Phys/DecayTreeTuple/src folder
