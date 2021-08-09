#Put in here all functions that build the different decay descriptors to be used


#Return list of "simplified" decay descriptors for a given HLT2 + extrasel combination
def get_combo_decaydescriptor(linename, hadron_comb, extrasel):
    charged_descriptor = [
        "B+ -> B0 pi+",
        "B- -> B0 pi-",
    ]
    neutral_descriptor = [
        "B0 -> B+ pi-",
        "B~0 -> B- pi+",
    ]
    decaydescriptor = {}
    #HHGamma
    decaydescriptor["HHGamma_hh_ExtraHadron_Combo"] = charged_descriptor
    decaydescriptor["HHGamma_hKs0_ExtraHadron_Combo"] = neutral_descriptor
    decaydescriptor["HHGamma_hL0_ExtraHadron_Combo"] = neutral_descriptor
    #HHGammaEE
    decaydescriptor["HHGammaEE_hh_ExtraHadron_Combo"] = charged_descriptor
    decaydescriptor["HHGammaEE_hKs0_ExtraHadron_Combo"] = neutral_descriptor
    decaydescriptor["HHGammaEE_hL0_ExtraHadron_Combo"] = neutral_descriptor
    return decaydescriptor["{0}_{1}_{2}_Combo".format(linename, hadron_comb,
                                                      extrasel)]


#Returns full decay descriptor for a given key
def get_full_decaydescriptor(linename):
    full_decaydescriptor = {}
    ##HHGamma descriptors
    full_decaydescriptor[
        "HHGamma_hh"] = "B0 -> ^(K*(892)0 -> ^pi+ ^pi-) ^gamma"
    full_decaydescriptor[
        "HHGamma_hKs0"] = "(B+ -> ^(K*(892)+ -> ^pi+ ^(KS0 -> ^pi+ ^pi-)) ^gamma) || (B- -> ^(K*(892)- -> ^pi- ^(KS0 -> ^pi+ ^pi-)) ^gamma)"
    full_decaydescriptor[
        "HHGamma_hL0"] = "(B+ -> ^(K*(892)+ -> ^pi+ ^(Lambda0 -> ^p+ ^pi-)) ^gamma) || (B- -> ^(K*(892)- -> ^pi- ^(Lambda~0 -> ^p~- ^pi+)) ^gamma)"
    ##HHGammaEE descriptors
    full_decaydescriptor[
        "HHGammaEE_hh"] = "B0 -> ^(K*(892)0 -> ^pi+ ^pi-) ^(gamma -> ^e+ ^e-)"
    full_decaydescriptor[
        "HHGammaEE_hKs0"] = "(B+ -> ^(K*(892)+ -> ^pi+ ^(KS0 -> ^pi+ ^pi-)) ^(gamma -> ^e+ ^e-)) || (B- -> ^(K*(892)- -> ^pi- ^(KS0 -> ^pi+ ^pi-)) ^(gamma -> ^e+ ^e-))"
    full_decaydescriptor[
        "HHGammaEE_hL0"] = "(B+ -> ^(K*(892)+ -> ^pi+ ^(Lambda0 -> ^p+ ^pi-)) ^(gamma -> ^e+ ^e-)) || (B- -> ^(K*(892)- -> ^pi- ^(Lambda~0 -> ^p~- ^pi+)) ^(gamma -> ^e+ ^e-))"
    #HHHGamma descriptors
    full_decaydescriptor[
        "HHHGamma_hhh"] = "(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^gamma) || (B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^gamma)"
    #HHHGammaEE descriptors
    full_decaydescriptor[
        "HHHGammaEE_hhh"] = "(B+ -> ^(D*(2010)+ -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi+) ^(gamma -> ^e+ ^e-)) || (B- -> ^(D*(2010)- -> ^(K*(892)0 -> ^pi+ ^pi-) ^pi-) ^(gamma -> ^e+ ^e-))"
    full_decaydescriptor["ExtraHadron"] = "(pi+) || (pi-)"
    full_decaydescriptor["ExtraKs0"] = "KS0 -> ^pi+ ^pi-"
    full_decaydescriptor[
        "ExtraLambda"] = "(Lambda0 -> ^p+ ^pi-) || (Lambda~0 -> ^p~- ^pi+)"
    full_decaydescriptor["ExtraGamma"] = "gamma"
    full_decaydescriptor["ExtraPi0Merged"] = "pi0"
    full_decaydescriptor["ExtraPi0Resolved"] = "pi0 -> ^gamma ^gamma"
    full_decaydescriptor[
        "HHGamma_hh_ExtraHadron_Combo"] = "(B+ -> ^({0}) ^pi+) || (B- -> ^({0}) ^pi-)".format(
            full_decaydescriptor["HHGamma_hh"])
    full_decaydescriptor[
        "HHGamma_hKs0_ExtraHadron_Combo"] = "(B0 -> ^(B+ -> ^(K*(892)+ -> ^pi+ ^(KS0 -> ^pi+ ^pi-)) ^gamma) ^pi-) || (B~0 -> ^(B- -> ^(K*(892)- -> ^pi- ^(KS0 -> ^pi+ ^pi-)) ^gamma) ^pi+)"
    full_decaydescriptor[
        "HHGamma_hL0_ExtraHadron_Combo"] = "(B0 -> ^(B+ -> ^(K*(892)+ -> ^pi+ ^(Lambda0 -> ^p+ ^pi-)) ^gamma) ^pi-) || (B~0 -> ^(B- -> ^(K*(892)- -> ^pi- ^(Lambda~0 -> ^p~- ^pi+)) ^gamma) ^pi+)"
    full_decaydescriptor[
        "HHGammaEE_hh_ExtraHadron_Combo"] = "(B+ -> ^({0}) ^pi+) || (B- -> ^({0}) ^pi-)".format(
            full_decaydescriptor["HHGammaEE_hh"])
    full_decaydescriptor[
        "HHGammaEE_hKs0_ExtraHadron_Combo"] = "(B0 -> ^(B+ -> ^(K*(892)+ -> ^pi+ ^(KS0 -> ^pi+ ^pi-)) ^(gamma -> ^e+ ^e-)) ^pi-) || (B~0 -> ^(B- -> ^(K*(892)- -> ^pi- ^(KS0 -> ^pi+ ^pi-)) ^(gamma -> ^e+ ^e-)) ^pi+)"
    full_decaydescriptor[
        "HHGammaEE_hL0_ExtraHadron_Combo"] = "(B0 -> ^(B+ -> ^(K*(892)+ -> ^pi+ ^(Lambda0 -> ^p+ ^pi-)) ^(gamma -> ^e+ ^e-)) ^pi-) || (B~0 -> ^(B- -> ^(K*(892)- -> ^pi- ^(Lambda~0 -> ^p~- ^pi+)) ^(gamma -> ^e+ ^e-)) ^pi+)"
    return full_decaydescriptor[linename]


#Returns branches for a given key
def get_branches(linename):
    branches = {}
    #Branches for HHGamma line
    branches["HHGamma_hh"] = {
        "B": "B0 -> (K*(892)0 -> pi+ pi-) gamma",
        "Kst": "B0 -> ^(K*(892)0 -> pi+ pi-) gamma",
        "piplus": "B0 -> (K*(892)0 -> ^pi+ pi-) gamma",
        "piminus": "B0 -> (K*(892)0 -> pi+ ^pi-) gamma",
        "gamma": "B0 -> (K*(892)0 -> pi+ pi-) ^gamma",
    }
    branches["HHGamma_hKs0"] = {
        "B":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> pi+ pi-)) gamma) || (B- -> (K*(892)- -> pi- (KS0 -> pi+ pi-)) gamma)",
        "Kst":
        "(B+ -> ^(K*(892)+ -> pi+ (KS0 -> pi+ pi-)) gamma) || (B- -> ^(K*(892)- -> pi- (KS0 -> pi+ pi-)) gamma)",
        "piplus":
        "(B+ -> (K*(892)+ -> ^pi+ (KS0 -> pi+ pi-)) gamma) || (B- -> (K*(892)- -> ^pi- (KS0 -> pi+ pi-)) gamma)",
        "Ks0":
        "(B+ -> (K*(892)+ -> pi+ ^(KS0 -> pi+ pi-)) gamma) || (B- -> (K*(892)- -> pi- ^(KS0 -> pi+ pi-)) gamma)",
        "piplus0":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> ^pi+ pi-)) gamma) || (B- -> (K*(892)- -> pi- (KS0 -> ^pi+ pi-)) gamma)",
        "piminus0":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> pi+ ^pi-)) gamma) || (B- -> (K*(892)- -> pi- (KS0 -> pi+ ^pi-)) gamma)",
        "gamma":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> pi+ pi-)) ^gamma) || (B- -> (K*(892)- -> pi- (KS0 -> pi+ pi-)) ^gamma)",
    }
    branches["HHGamma_hL0"] = {
        "B":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> p+ pi-)) gamma) || (B- -> (K*(892)- -> pi- (Lambda~0 -> p~- pi+)) gamma)",
        "Kst":
        "(B+ -> ^(K*(892)+ -> pi+ (Lambda0 -> p+ pi-)) gamma) || (B- -> ^(K*(892)- -> pi- (Lambda~0 -> p~- pi+)) gamma)",
        "piplus":
        "(B+ -> (K*(892)+ -> ^pi+ (Lambda0 -> p+ pi-)) gamma) || (B- -> (K*(892)- -> ^pi- (Lambda~0 -> p~- pi+)) gamma)",
        "Lambda0":
        "(B+ -> (K*(892)+ -> pi+ ^(Lambda0 -> p+ pi-)) gamma) || (B- -> (K*(892)- -> pi- ^(Lambda~0 -> p~- pi+)) gamma)",
        "pplus":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> ^p+ pi-)) gamma) || (B- -> (K*(892)- -> pi- (Lambda~0 -> ^p~- pi+)) gamma)",
        "piminus0":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> p+ ^pi-)) gamma) || (B- -> (K*(892)- -> pi- (Lambda~0 -> p~- ^pi+)) gamma)",
        "gamma":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> p+ pi-)) ^gamma) || (B- -> (K*(892)- -> pi- (Lambda~0 -> p~- pi+)) ^gamma)",
    }
    #Branches for HHGammaEE line
    branches["HHGammaEE_hh"] = {
        "B": "B0 -> (K*(892)0 -> pi+ pi-) (gamma-> e+ e-)",
        "Kst": "B0 -> ^(K*(892)0 -> pi+ pi-) (gamma-> e+ e-)",
        "piplus": "B0 -> (K*(892)0 -> ^pi+ pi-) (gamma-> e+ e-)",
        "piminus": "B0 -> (K*(892)0 -> pi+ ^pi-) (gamma-> e+ e-)",
        "gamma": "B0 -> (K*(892)0 -> pi+ pi-) ^(gamma-> e+ e-)",
        "eplus": "B0 -> (K*(892)0 -> pi+ pi-) (gamma-> ^e+ e-)",
        "eminus": "B0 -> (K*(892)0 -> pi+ pi-) (gamma-> e+ ^e-)",
    }
    branches["HHGammaEE_hKs0"] = {
        "B":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> pi+ pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- (KS0 -> pi+ pi-)) (gamma-> e+ e-))",
        "Kst":
        "(B+ -> ^(K*(892)+ -> pi+ (KS0 -> pi+ pi-)) (gamma-> e+ e-)) || (B- -> ^(K*(892)- -> pi- (KS0 -> pi+ pi-)) (gamma-> e+ e-))",
        "piplus":
        "(B+ -> (K*(892)+ -> ^pi+ (KS0 -> pi+ pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> ^pi- (KS0 -> pi+ pi-)) (gamma-> e+ e-))",
        "Ks0":
        "(B+ -> (K*(892)+ -> pi+ ^(KS0 -> pi+ pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- ^(KS0 -> pi+ pi-)) (gamma-> e+ e-))",
        "piplus0":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> ^pi+ pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- (KS0 -> ^pi+ pi-)) (gamma-> e+ e-))",
        "piminus0":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> pi+ ^pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- (KS0 -> pi+ ^pi-)) (gamma-> e+ e-))",
        "gamma":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> pi+ pi-)) ^(gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- (KS0 -> pi+ pi-)) ^(gamma-> e+ e-))",
        "eplus":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> pi+ pi-)) (gamma-> ^e+ e-)) || (B- -> (K*(892)- -> pi- (KS0 -> pi+ pi-)) (gamma-> ^e+ e-))",
        "eminus":
        "(B+ -> (K*(892)+ -> pi+ (KS0 -> pi+ pi-)) (gamma-> e+ ^e-)) || (B- -> (K*(892)- -> pi- (KS0 -> pi+ pi-)) (gamma-> e+ ^e-))",
    }
    branches["HHGammaEE_hL0"] = {
        "B":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> p+ pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- (Lambda~0 -> p~- pi+)) (gamma-> e+ e-))",
        "Kst":
        "(B+ -> ^(K*(892)+ -> pi+ (Lambda0 -> p+ pi-)) (gamma-> e+ e-)) || (B- -> ^(K*(892)- -> pi- (Lambda~0 -> p~- pi+)) (gamma-> e+ e-))",
        "piplus":
        "(B+ -> (K*(892)+ -> ^pi+ (Lambda0 -> p+ pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> ^pi- (Lambda~0 -> p~- pi+)) (gamma-> e+ e-))",
        "Lambda0":
        "(B+ -> (K*(892)+ -> pi+ ^(Lambda0 -> p+ pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- ^(Lambda~0 -> p~- pi+)) (gamma-> e+ e-))",
        "pplus":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> ^p+ pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- (Lambda~0 -> ^p~- pi+)) (gamma-> e+ e-))",
        "piminus0":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> p+ ^pi-)) (gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- (Lambda~0 -> p~- ^pi+)) (gamma-> e+ e-))",
        "gamma":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> p+ pi-)) ^(gamma-> e+ e-)) || (B- -> (K*(892)- -> pi- (Lambda~0 -> p~- pi+)) ^(gamma-> e+ e-))",
        "eplus":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> p+ pi-)) (gamma-> ^e+ e-)) || (B- -> (K*(892)- -> pi- (Lambda~0 -> p~- pi+)) (gamma-> ^e+ e-))",
        "eminus":
        "(B+ -> (K*(892)+ -> pi+ (Lambda0 -> p+ pi-)) (gamma-> e+ ^e-)) || (B- -> (K*(892)- -> pi- (Lambda~0 -> p~- pi+)) (gamma-> e+ ^e-))",
    }
    #Branches for HHHGamma line
    branches["HHHGamma_hhh"] = {
        "B":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) gamma)",
        "Dst":
        "(B+ -> ^(D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) gamma) || (B- -> ^(D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) gamma)",
        "Kst":
        "(B+ -> (D*(2010)+ -> ^(K*(892)0 -> pi+ pi-) pi+) gamma) || (B- -> (D*(2010)- -> ^(K*(892)0 -> pi+ pi-) pi-) gamma)",
        "pi3":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) ^pi+) gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) ^pi-) gamma)",
        "piplus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> ^pi+ pi-) pi+) gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> ^pi+ pi-) pi-) gamma)",
        "piminus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ ^pi-) pi+) gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) ^pi-) gamma)",
        "gamma":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) ^gamma) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) ^gamma)",
    }
    #Branches for HHHGammaEE line
    branches["HHHGammaEE_hhh"] = {
        "B":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) (gamma -> e+ e-))",
        "Dst":
        "(B+ -> ^(D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) (gamma -> e+ e-)) || (B- -> ^(D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) (gamma -> e+ e-))",
        "Kst":
        "(B+ -> (D*(2010)+ -> ^(K*(892)0 -> pi+ pi-) pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> ^(K*(892)0 -> pi+ pi-) pi-) (gamma -> e+ e-))",
        "pi3":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) ^pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) ^pi-) (gamma -> e+ e-))",
        "piplus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> ^pi+ pi-) pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> ^pi+ pi-) pi-) (gamma -> e+ e-))",
        "piminus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ ^pi-) pi+) (gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) ^pi-) (gamma -> e+ e-))",
        "gamma":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) ^(gamma -> e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) ^(gamma -> e+ e-))",
        "eplus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) (gamma -> ^e+ e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) (gamma -> ^e+ e-))",
        "eminus":
        "(B+ -> (D*(2010)+ -> (K*(892)0 -> pi+ pi-) pi+) (gamma -> e+ ^e-)) || (B- -> (D*(2010)- -> (K*(892)0 -> pi+ pi-) pi-) (gamma -> e+ ^e-))",
    }
    #Branches for ExtraHadron
    branches["ExtraHadron"] = {"pi": "(pi+) || (pi-)"}
    #Branches for ExtraKs0
    branches["ExtraKs0"] = {
        "Ks0": "KS0 -> pi+ pi-",
        "piplus": "KS0 -> ^pi+ pi-",
        "piminus": "KS0 -> pi+ ^pi-",
    }
    #Branches for ExtraLambda
    branches["ExtraLambda"] = {
        "Lambda": "(Lambda0 -> p+ pi-) || (Lambda~0 -> p~- pi+)",
        "pplus": "(Lambda0 -> ^p+ pi-) || (Lambda~0 -> ^p~- pi+)",
        "piminus": "(Lambda0 -> p+ ^pi-) || (Lambda~0 -> p~- ^pi+)",
    }
    #Branches for ExtraGamma
    branches["ExtraGamma"] = {
        "gamma": "gamma",
    }
    #Branches for ExtraPi0Merged
    branches["ExtraPi0Merged"] = {
        "pi0": "pi0",
    }
    #Branches for ExtraPi0Resolved
    branches["ExtraPi0Resolved"] = {
        "pi0": "pi0 -> gamma gamma",
        "gamma1": "pi0 -> ^gamma gamma",
        "gamma2": "pi0 -> gamma ^gamma",
    }
    return branches[linename]