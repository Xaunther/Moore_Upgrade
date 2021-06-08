onerror:
    print("errors have ocurred, please check everything")

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
    "KstG"    :  "Kplus,piminus",
    "PhiG"    :  "Kplus,Kminus",
    "K1G"     :  "Kplus,piminus,piplus",
    "LambdaG" :  "pplus,piminus",
    "XiG"     :  "pplus,piminus,piminus0",
    "OmegaG"  :  "pplus,piminus,Kminus"
}

#List of extra selection containers
extra_container_list = ["ExtraHadron", "ExtraKs0", "ExtraLambda", "ExtraGamma", "ExtraPi0Merged", "ExtraPi0Resolved"]


# ------ #
# RULES
# ------ #

################################### Input options files ###################################

rule all_LFNs:
    input: expand("Gaudi_inputs/{MC}_input_LFNs.py", MC=MC_list)

rule get_LFN:
    output: "Gaudi_inputs/{MC}_input_LFNs.py"
    params:
        prodID=lambda wcs: prodIDs[wcs.MC]
    shell:
        "lb-dirac dirac-bookkeeping-get-files --Prod {params.prodID} --OptionsFile {output}"

rule all_PFNs:
    input: expand("Gaudi_inputs/{MC}_input_PFNs.py", MC=MC_list)

rule get_PFN:
    input: "Gaudi_inputs/{MC}_input_LFNs.py"
    output: "Gaudi_inputs/{MC}_input_PFNs.py"
    shell:
        "lb-dirac dirac-bookkeeping-genXMLCatalog --Options {input} --NewOptions {output}"

################################### MOORE ANALYSIS PART ###################################
rule all_MA:
    input:
        expand("Gaudi_inputs/{MC}_input_LFNs.py", MC=MC_list),
        expand("Gaudi_inputs/{MC}_input_PFNs.py", MC=MC_list),
        expand("output/{MC}/AllLines_MA.root", MC=MC_list),
        expand("output/{MC}/AllLines_eff_MA.txt", MC=MC_list),
        expand("output/{MC}/CorrelationMatrix_MA.md", MC=MC_list)


#Produce ntuples from MooreAnalysis.
#They produce MCDecayTreeTuples so all possible events that can be reconstructed with MC matching,
#just FLAGGING whether they pass the HLT lines of interest or not
rule alltuples_MA:
    input: expand("output/{MC}/AllLines_MA.root", MC=MC_list)
    # input: "output/KstG/AllLines_MA.root"

rule MA_tuple:
    input: "Gaudi_inputs/{MC}_input_PFNs.py"
    output: "output/{MC}/AllLines_MA.root"
    run:
        shell('mkdir -p output/{wildcards.MC}')
        ma_script = f'{MOOREANALYSIS}/run gaudirun.py MooreAnalysis_Scripts/{wildcards.MC}.py'
        options   = f' options/2000_Evts.py MooreAnalysis_Scripts/AllLines.py Gaudi_inputs/{wildcards.MC}_input_PFNs.py'
        tee       = f' | tee output/{wildcards.MC}/AllLines_MA.out'
        try:
            shell("set +e")
            shell(ma_script+options+tee)
            shell('touch tmp_check.txt')
        except:
            print("except: errors during MA_tuple")
    # shell:
    #     'mkdir -p output/{wildcards.MC} \n'
    #     '{MOOREANALYSIS}/run gaudirun.py MooreAnalysis_Scripts/{wildcards.MC}.py '
    #     ' options/2000_Evts.py MooreAnalysis_Scripts/AllLines.py Gaudi_inputs/{wildcards.MC}_input_PFNs.py '
    #     ' | tee output/{wildcards.MC}/AllLines_MA.out'


#Produce efficiency results by using the ntuple info
#We use reconstructible children, which only takes children with pseudorapidity in LHCb range
rule alleffs_MA:
    input: expand("output/{MC}/AllLines_eff_MA.txt", MC=MC_list)
    # input: "output/KstG/AllLines_eff_MA.txt"

rule MA_efficience:
    input: "output/{MC}/AllLines_MA.root"
    output: "output/{MC}/AllLines_eff_MA.txt"
    params:
        reconstructibles=lambda wcs: reconstructibles_d[wcs.MC]
    # run:
    #     shell('mkdir -p output/{wildcards.MC}')
    #     ma_script = f'{MOOREANALYSIS}/run {MOOREANALYSIS}/HltEfficiencyChecker/scripts/hlt_line_efficiencies.py'
    #     options   = f' {input} --level Hlt2 --reconstructible-children={params.reconstructibles}'
    #     tee       = f' | tee {output}'
    #     shell(ma_script+options+tee)
    shell:
        'mkdir -p output/{wildcards.MC} \n'
        '{MOOREANALYSIS}/run {MOOREANALYSIS}/HltEfficiencyChecker/scripts/hlt_line_efficiencies.py'
        ' {input} --level Hlt2 --reconstructible-children={params.reconstructibles}'
        ' | tee {output}'

#Another thing, get correlation matrices for the 4 trigger lines, in each MC
rule allcorrelations_MA:
    input: expand("output/{MC}/CorrelationMatrix_MA.md", MC=MC_list)
    # input: "output/KstG/CorrelationMatrix_MA.md"

rule MA_correlation:
    input: "output/{MC}/AllLines_MA.root", "Cuts/HLT2_radiative_cuts.txt"
    output: "output/{MC}/CorrelationMatrix_MA.md"
    shell:
        '{ANALYSIS_TOOLS_ROOT}/CutCorrelation.out {input} {output} MCDecayTreeTuple/MCDecayTree'


################################### MOORE PART ###################################
rule all_Moore:
    input:
        expand("output/{MC}/AllLines_Moore.mdst", MC=MC_list)
# .PHONY: allDSTs_Moore allEvtSizes_Moore alltuples_Moore


#Produce DSTs from Moore.
#They produce FILTERED DSTs where only events that pass any HLT line are stored.
rule allDSTs_Moore:
    input: expand("output/{MC}/AllLines_Moore.mdst", MC=MC_list)

rule Dst_Moore:
    input: "Gaudi_inputs/{MC}_input_PFNs.py"
    output: "output/{MC}/AllLines_Moore.mdst"
    shell:
        "mkdir -p output/{wildcards.MC} \n"
        "{MOORE}/run gaudirun.py Moore_Scripts/{wildcards.MC}.py "
        "options/2000_Evts.py Moore_Scripts/AllLines.py Gaudi_inputs/{wildcards.MC}_input_PFNs.py "
        "| tee output/{wildcards.MC}/AllLines_Moore.out \n"
        "rm -f test_catalog.xml"

# #Once the mDSTs have been produced, we can run a hacked script from upgrade-bandwidth-studies
rule allEvtSizes_Moore:
    input: expand("output/{MC}/AllLines_EvtSize_Moore.txt", MC=MC_list)

rule EvtSize_Moore:
    input: "output/{MC}/AllLines_Moore.mdst"
    output: "output/{MC}/AllLines_EvtSize_Moore.txt"
    shell:
        "{MOORE}/run python scripts/event_size.py {input} "
        "| tee {output}"


# #Time to produce ntuples
rule allTuples_Moore:
    input: expand("output/{MC}/AllLines_Moore.root", MC=MC_list)

rule Tuple_Moore:
    input: "output/{MC}/AllLines_Moore.mdst"
    output: "output/{MC}/AllLines_Moore.root"
    shell:
        "{DAVINCI}/run gaudirun.py DaVinci_Scripts/{wildcards.MC}.py DaVinci_Scripts/AllLines.py"

#For each line, we loop over all the containers
lines = ["HHGamma","HHGammaEE","HHHGamma","HHGammaEE"]

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

rule lines_multiplicities:
    input:
        expand("output/multiplicities/{line}_{extra}_multiplicity.txt",
            line=lines,extra=extra_container_list)

# #HHGamma
# rule HHGamma_extra_multiplicities:
#     input:
#         tuples= expand("output/{MC}/AllLines_Moore.root", MC=MC_list),
#         cuts=   "Cuts/{extra}_cuts.txt",
#     output:
#         "output/multiplicities/HHGamma_{extra}_multiplicity.txt"
#     shell:
#         '{ANALYSIS_TOOLS_ROOT}/Multiplicity_Extrasel.out "{input.tuples}" '
#         ' Cuts/{wildcards.extra}_cuts.txt {output} HHGammaTuple/DecayTree HHGamma_{wildcards.extra}Tuple/DecayTree '

# rule HHGamma_multiplicities:
#     input: expand("output/multiplicities/HHGamma_{extra}_multiplicity.txt",extra=extra_container_list)
