# Snakemake for moore_upgrade

#Stack installation
STACKDIR="../stack"
MOOREANALYSIS = STACKDIR + "/MooreAnalysis"
MOORE = STACKDIR + "/Moore"
DAVINCI = STACKDIR + "/DaVinci"

#Where folder with root scripts (https://gitlab.cern.ch/aalfonso-Analysis-Tools/root) resides
#Needs compilation before running
ANALYSIS_TOOLS_ROOT= "../root"

#List of MC samples available
MC_list=["KstG", "PhiG", "K1G", "LambdaG", "XiG", "OmegaG"] # "KstG", "PhiG", "K1G", "LambdaG", "XiG", "OmegaG"
lines = ["HHGamma","HHGammaEE","HHHGamma","HHGammaEE"]

# Production IDs for each MC
prodIDs={
    "KstG"   :  "75829",
    "PhiG"   :  "75812",
    "K1G"    :  "75816",
    "LambdaG":  "76702",
    "XiG"    :  "109825",
    "OmegaG" :  "109823",
    "PhiKstG_prodID"        : "133775",
    "PhiPhiG_prodID"        : "133773",
    "PhiKs0G_prodID"        : "133769",
    "K1G_KPiPi0_prodID"     : "133765",
    "PhiPi0G_prodID"        : "133763",
    "KstIsoG_prodID"        : "133761",
    "LambdaPG_prodID"       : "133759",
    "PhiKG_prodID"          : "133753",
    "K1G_Cocktail_prodID"   : "133757",
    "L1520G_prodID"         : "133755",
    "RhoG_prodID"           : "133751"
}

# Reconstructibles for each MC
reconstructibles_d={
    "KstG"    :  "Kplus,piminus",
    "PhiG"    :  "Kplus,Kminus",
    "K1G"     :  "Kplus,piminus,piplus",
    "LambdaG" :  "pplus,piminus",
    "XiG"     :  "pplus,piminus,piminus0",
    "OmegaG"  :  "pplus,piminus,Kminus",
    "PhiKstG_reconstructibles"      : "Kplus,Kminus,Kplus0,piminus",
    "PhiPhiG_reconstructibles"      : "Kplus,Kminus,Kplus0,Kminus0",
    "PhiKs0G_reconstructibles"      : "Kplus,Kminus,piplus,piminus",
    "K1G_KPiPi0_reconstructibles"   : "Kplus,piminus",
    "PhiPi0G_reconstructibles"      : "Kplus,Kminus",
    "KstIsoG_reconstructibles"      : "piplus,piminus,piplus0",
    "LambdaPG_reconstructibles"     : "pminus,piplus,pplus",
    "PhiKG_reconstructibles"        : "Kplus,Kminus,Kplus0",
    "K1G_Cocktail_reconstructibles" : "Kplus,piminus,piplus",
    "L1520G_reconstructibles"       : "pplus,Kminus",
    "RhoG_reconstructibles"         : "piplus,piminus"
}

#List of extra selection containers
extra_container_list = ["ExtraHadron", "ExtraKs0", "ExtraLambda", "ExtraGamma", "ExtraPi0Merged", "ExtraPi0Resolved"]


# ------ #
# RULES
# ------ #

onerror:
    print("errors have ocurred, please check everything")

################################### ALL ###################################
rule all:
    """All MooreAnalysis and all Moore"""
    input:
        expand("Gaudi_inputs/{MC}_input_LFNs.py", MC=MC_list),
        expand("Gaudi_inputs/{MC}_input_PFNs.py", MC=MC_list),
        expand("output/{MC}/AllLines_MA.root", MC=MC_list),
        report(expand("output/{MC}/AllLines_eff_MA.txt", MC=MC_list)),
        report(expand("output/{MC}/CorrelationMatrix_MA.md", MC=MC_list)),
        expand("output/{MC}/AllLines_Moore.mdst", MC=MC_list),
        report(expand("output/{MC}/AllLines_EvtSize_Moore.txt", MC=MC_list)),
        expand("output/{MC}/AllLines_Moore.root", MC=MC_list),
        expand("output/multiplicities/{line}_{extra}_multiplicity.txt",
            line=lines,extra=extra_container_list)


################################### Input options files ###################################
#Produce input scripts from the ProdIDs (these commands might need rerunning every few months to update PFNs)
rule all_LFNs:
    """ get input LFNs from prodID"""
    input: expand("Gaudi_inputs/{MC}_input_LFNs.py", MC=MC_list)

rule get_LFN:
    """This is a prerrequisite for both MooreAnalysis and Moore workflows
    First, get input LFNs from prodID
    """
    #Warning (2021/08/05) only works in lxplus, but not in ubuntu + docker
    output: "Gaudi_inputs/{MC}_input_LFNs.py"
    params:
        prodID=lambda wcs: prodIDs[wcs.MC]
    shell:
        "lb-dirac dirac-bookkeeping-get-files --Prod={params.prodID} --OptionsFile={output}"

rule all_PFNs:
    """translate the LFN list into a PFN list which can be used in Gaudi software"""
    input: expand("Gaudi_inputs/{MC}_input_PFNs.py", MC=MC_list)

rule get_PFN:
    input: "Gaudi_inputs/{MC}_input_LFNs.py"
    output: "Gaudi_inputs/{MC}_input_PFNs.py"
    shell:
        "lb-dirac dirac-bookkeeping-genXMLCatalog --Options={input} --NewOptions={output}"


################################### MOORE ANALYSIS PART ###################################
rule all_MA:
    input:
        expand("Gaudi_inputs/{MC}_input_LFNs.py", MC=MC_list),
        expand("Gaudi_inputs/{MC}_input_PFNs.py", MC=MC_list),
        expand("output/{MC}/AllLines_MA.root", MC=MC_list),
        report(expand("output/{MC}/AllLines_eff_MA.txt", MC=MC_list)),
        report(expand("output/{MC}/CorrelationMatrix_MA.md", MC=MC_list))


rule alltuples_MA:
    """
    Produce ntuples from MooreAnalysis.
    They produce MCDecayTreeTuples so all possible events that can be reconstructed with MC matching,
    just FLAGGING whether they pass the HLT lines of interest or not
    """
    input: expand("output/{MC}/AllLines_MA.root", MC=MC_list)

rule MA_tuple:
    input: "Gaudi_inputs/{MC}_input_PFNs.py"
    output: "output/{MC}/AllLines_MA.root"
    run:
        shell('mkdir -p output/{wildcards.MC}')
        ma_script = f'{MOOREANALYSIS}/run  --set=DECAY={wildcards.MC} gaudirun.py options/Decay_options.py'
        options   = f' options/2000_Evts.py MooreAnalysis_Scripts/AllLines.py Gaudi_inputs/{wildcards.MC}_input_PFNs.py'
        tee       = f' | tee output/{wildcards.MC}/AllLines_MA.out'
        try:
            shell("set +e")
            shell(ma_script+options+tee)
            shell("set -e")
        except:
            print("except: errors during MA_tuple")


rule alleffs_MA:
    """
    Produce efficiency results by using the ntuple info
    We use reconstructible children, which only takes children with pseudorapidity in LHCb range
    """
    input: expand("output/{MC}/AllLines_eff_MA.txt", MC=MC_list)

rule MA_efficience:
    input: "output/{MC}/AllLines_MA.root"
    output: "output/{MC}/AllLines_eff_MA.txt"
    params:
        reconstructibles=lambda wcs: reconstructibles_d[wcs.MC]
    shell:
        'mkdir -p output/{wildcards.MC} \n'
        '{MOOREANALYSIS}/run {MOOREANALYSIS}/HltEfficiencyChecker/scripts/hlt_line_efficiencies.py'
        ' {input} --level Hlt2 --reconstructible-children={params.reconstructibles}'
        ' | tee {output}'


rule allcorrelations_MA:
    """get correlation matrices for the 4 trigger lines, in each MC"""
    input: expand("output/{MC}/CorrelationMatrix_MA.md", MC=MC_list)

rule MA_correlation:
    input: "output/{MC}/AllLines_MA.root", "Cuts/HLT2_radiative_cuts.txt"
    output: "output/{MC}/CorrelationMatrix_MA.md"
    shell:
        '{ANALYSIS_TOOLS_ROOT}/CutCorrelation.out {input} {output} MCDecayTreeTuple/MCDecayTree'


################################### MOORE PART ###################################
rule all_Moore:
    input:
        expand("output/{MC}/AllLines_Moore.mdst", MC=MC_list),
        report(expand("output/{MC}/AllLines_EvtSize_Moore.txt", MC=MC_list)),
        expand("output/{MC}/AllLines_Moore.root", MC=MC_list),
        report(expand("output/multiplicities/{line}_{extra}_multiplicity.txt",
            line=lines,extra=extra_container_list))

rule allDSTs_Moore:
    """
    Produce DSTs from Moore.
    They produce FILTERED DSTs where only events that pass any HLT line are stored.
    """
    input: expand("output/{MC}/AllLines_Moore.mdst", MC=MC_list)

rule Dst_Moore:
    input: "Gaudi_inputs/{MC}_input_PFNs.py"
    output: "output/{MC}/AllLines_Moore.mdst"
    shell:
        "mkdir -p output/{wildcards.MC} \n"
        "{MOORE}/run --set=DECAY={wildcards.MC} gaudirun.py options/Decay_options.py "
        "options/2000_Evts.py Moore_Scripts/AllLines.py Gaudi_inputs/{wildcards.MC}_input_PFNs.py "
        "| tee output/{wildcards.MC}/AllLines_Moore.out \n"
        "rm -f test_catalog*.xml"


rule allEvtSizes_Moore:
    """Once the mDSTs have been produced, we can run a hacked script from upgrade-bandwidth-studies"""
    #Make sure you have prettytable installed
    input: expand("output/{MC}/AllLines_EvtSize_Moore.txt", MC=MC_list)

rule EvtSize_Moore:
    input: "output/{MC}/AllLines_Moore.mdst"
    output: "output/{MC}/AllLines_EvtSize_Moore.txt"
    shell:
        "python scripts/event_size.py {input} | tee {output}"


rule allTuples_Moore:
    """Time to produce ntuples"""
    input: expand("output/{MC}/AllLines_Moore.root", MC=MC_list)

rule Tuple_Moore:
    input: "output/{MC}/AllLines_Moore.mdst"
    output: "output/{MC}/AllLines_Moore.root"
    shell:
        "{DAVINCI}/run --set=DECAY={wildcards.MC} gaudirun.py DaVinci_Scripts/Decay_options.py DaVinci_Scripts/AllLines.py"


rule lines_multiplicities:
    """For each line, we loop over all the containers"""
    input:
        expand("output/multiplicities/{line}_{extra}_multiplicity.txt",
            line=lines,extra=extra_container_list)

rule line_extra_multiplicities:
    input:
        tuples= expand("output/{MC}/AllLines_Moore.root", MC=MC_list),
        cuts=   "Cuts/{extra}_cuts.txt",
    output:
        "output/multiplicities/{line}_{extra}_multiplicity.txt"
    shell:
        '{ANALYSIS_TOOLS_ROOT}/Multiplicity_Extrasel.out "{input.tuples}" '
        ' Cuts/{wildcards.extra}_cuts.txt {output} {wildcards.line}Tuple/DecayTree'
        ' {wildcards.line}_{wildcards.extra}Tuple/DecayTree '

#HHGamma
rule HHGamma_extra_multiplicities:
    input:
        expand("output/multiplicities/HHGamma_{extra}_multiplicity.txt",
            extra=extra_container_list)
#HHGammaEE
rule HHGammaEE_extra_multiplicities:
    input:
        expand("output/multiplicities/HHGammaEE_{extra}_multiplicity.txt",
            extra=extra_container_list)
#HHHGamma
rule HHHGamma_extra_multiplicities:
    input:
        expand("output/multiplicities/HHHGamma_{extra}_multiplicity.txt",
            extra=extra_container_list)
#HHHGammaEE
rule HHHGammaEE_extra_multiplicities:
    input:
        expand("output/multiplicities/HHHGammaEE_{extra}_multiplicity.txt",
            extra=extra_container_list)
