#Fix LFNs from a list of MC keys. Warning, takes its time.
import os, sys

#Possibilities
Decay_keys = [
    "K1G_Cocktail_Down",
    "K1G_Cocktail_Up",
    "K1G_Down",
    "K1G_KPiPi0_Down",
    "K1G_KPiPi0_Up",
    "KstG_Down",
    "KstIsoG_Down",
    "KstIsoG_Up",
    "L1520G_Down",
    "L1520G_Up",
    "LambdaG_Down",
    "LambdaPG_Down",
    "LambdaPG_Up",
    "OmegaG_Down",
    "OmegaG_Up",
    "PhiG_Down",
    "PhiKG_Down",
    "PhiKG_Up",
    "PhiKs0G_Down",
    "PhiKs0G_Up",
    "PhiKstG_Down",
    "PhiKstG_Up",
    "PhiPhiG_Down",
    "PhiPhiG_Up",
    "PhiPi0G_Down",
    "PhiPi0G_Up",
    "RhoG_Down",
    "RhoG_Up",
    "XiG_Down",
    "XiG_Up",
    "MinBias_Down",
]


#Function that returns list of LFNs in a list, with "LFN:"" prefix removed
def GetLFNs(filename):

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    LFNs = []
    for line in lines:
        LFNs.append(line.rstrip("\n").strip("LFN:"))
    return LFNs


#Requested keys blank-space separated
requested_keys = sys.argv[1:]

#We must loop over each key requested
for req_key in requested_keys:
    #If invalid, skip to next
    try:
        Decay_keys.index(req_key)
    except KeyError:
        print("{key} not found. Skipping...".format(key=req_key))
        continue
    #If the key is ok, get the list of LFN files
    print("Starting reading {key} LFNs".format(key=req_key))
    print("---------------------------")
    LFNs = GetLFNs(
        "ganga_Scripts/ganga_DaVinci_LFNs/{key}".format(key=req_key))

    #We create the output folder for the .root
    os.system("mkdir -p ganga_Scripts/ganga_DaVinci_ntuples/{key}".format(
        key=req_key))

    #Now we must loop over this list of LFNs, and run the dirac command to download.
    #Also need to assign a unique name to it
    for i in range(len(LFNs)):
        os.system(
            "lb-dirac dirac-dms-get-file {lfn} -D ganga_Scripts/ganga_DaVinci_ntuples/{key}"
            .format(
                lfn=LFNs[i],
                key=req_key,
            ))
        os.system(
            "mv AllLines_Moore.root ganga_Scripts/ganga_DaVinci_ntuples/{key}/AllLines_Moore_{i}.root"
            .format(
                i=str(i),
                key=req_key,
            ))
