# Fix for TupleToolGeometry

TupleToolGeometry is unable to recover the list of PVs as it is (2021-08-26). This is a fix in order to be able to recover them. Just copy TupleToolGeometry.cpp (.h) into Phys/DecayTreeTuple/src inside (folder checked out from Analysis)

It works with DaVinci v52r0, but for some reason v54r0 breaks simply when checking out Phys/DecayTreeTuple (the includes are not being found, I hope they'll fix it)