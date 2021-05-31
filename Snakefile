
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
MC_list=["KstG", "PhiG", "K1G", "LambdaG", "XiG", "OmegaG"]

# Production IDs for each MC
prodIDs={
    "KstG"   :  "75829",
    "PhiG"   :  "75812",
    "K1G"    :  "75816",
    "LambdaG":  "76702",
    "XiG"    :  "109825",
    "OmegaG" :  "109823"
}

# Reconstructibles for each MC
reconstructibles_d={
    KstG    :  ["Kplus","piminus"],
    PhiG    :  ["Kplus","Kminus"],
    K1G     :  ["Kplus","piminus","piplus"],
    LambdaG :  ["pplus","piminus"],
    XiG     :  ["pplus","piminus","piminus0"],
    OmegaG  :  ["pplus","piminus","Kminus"]
}

#List of extra selection containers
extra_container_list = ["ExtraHadron", "ExtraKs0", "ExtraLambda", "ExtraGamma", "ExtraPi0Merged", "ExtraPi0Resolved"]


# ------ #
# RULES
# ------ #

################################### Input options files ###################################

rule get_all_LFNs:
    input: expand("Gaudi_inputs/{MC}_input_LFNs.py", MC=MC_list)

rule get_LFN:
    output: "Gaudi_inputs/{MC}_input_LFNs.py"
    params:
        prodID=lambda wcs: prodIDs[wcs.MC]
    run:
        prodid="{params.prodID}"
        shell('echo _Prod ID:__ '+prodid+' ___'  )
        shell(f"lb-dirac dirac-bookkeeping-get-files --Prod {prodid} --OptionsFile {output}")

rule get_all_PFNs:
    input: expand("Gaudi_inputs/{MC}_input_PFNs.py", MC=MC_list)

rule get_PFN:
    input: "Gaudi_inputs/{MC}_input_LFNs.py"
    output: "Gaudi_inputs/{MC}_input_PFNs.py"
    shell: "lb-dirac dirac-bookkeeping-genXMLCatalog --Options {input} --NewOptions {output}"

