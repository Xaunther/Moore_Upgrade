#Makefile to remember the different commands to run things

#Stack installation
STACKDIR=../LHCb/stack
MOOREANALYSIS=$(STACKDIR)/MooreAnalysis
MOORE=$(STACKDIR)/Moore
DAVINCI=$(STACKDIR)/DaVinci

#Where folder with root scripts (https://gitlab.cern.ch/aalfonso-Analysis-Tools/root) resides
#Needs compilation before running
ANALYSIS_TOOLS_ROOT=../root

#Folder with upgrade-bandwith-studies repo (https://gitlab.cern.ch/lhcb-HLT/upgrade-bandwidth-studies)
#Also needs compilation
UPGRADE_BANDWIDTH_STUDIES=../upgrade-bandwidth-studies

#List of MC samples available
MC_list=KstG PhiG K1G LambdaG XiG OmegaG

#List of reconstructibles for each MC
KstG_reconstructibles=Kplus,piminus
PhiG_reconstructibles=Kplus,Kminus
K1G_reconstructibles=Kplus,piminus,piplus
LambdaG_reconstructibles=pplus,piminus
XiG_reconstructibles=pplus,piminus,piminus0
OmegaG_reconstructibles=pplus,piminus,Kminus

#List of extra selection containers
extra_container_list=ExtraHadron ExtraKs0 ExtraLambda ExtraGamma ExtraPi0Merged ExtraPi0Resolved

#List of important make commands
all: all_MA all_Moore
#Produce efficiencies for all radiative lines and all radiative channels included in MC_list
.PHONY: all_MA
#Produce ntuples with events that pass at least one of a collection of HLT lines (FILTERING)
.PHONY: all_Moore

################################### MOORE ANALYSIS PART ###################################
#Produce ntuples from MooreAnalysis.
#They produce MCDecayTreeTuples so all possible events that can be reconstructed with MC matching,
#just FLAGGING whether they pass the HLT lines of interest or not
alltuple_MA_list = $(foreach MC, $(MC_list),output/$(MC)/AllLines_MA.root)
alltuples_MA: $(alltuple_MA_list)
$(alltuple_MA_list): output/%/AllLines_MA.root:
	mkdir -p output/$*
	$(MOOREANALYSIS)/run gaudirun.py MooreAnalysis_Scripts/$*.py MooreAnalysis_Scripts/AllLines.py

#Produce efficiency results by using the ntuple info
#We use reconstructible children, which only takes children with pseudorapidity in LHCb range
alleff_MA_list = $(foreach MC, $(MC_list),output/$(MC)/AllLines_eff_MA.txt)
alleffs_MA: $(alleff_MA_list)
$(alleff_MA_list): output/%/AllLines_eff_MA.txt: output/%/AllLines_MA.root
	$(MOOREANALYSIS)/run $(MOOREANALYSIS)/HltEfficiencyChecker/scripts/hlt_line_efficiencies.py $< --level Hlt2 --reconstructible-children=$($*_reconstructibles) > $@

#Run all Moore Analysis part
all_MA: alleffs_MA

################################### MOORE PART ###################################
#Produce DSTs from Moore.
#They produce FILTERED DSTs where only events that pass any HLT line are stored.
allDST_Moore_list=$(foreach MC, $(MC_list),output/$(MC)/AllLines_Moore.mdst)
allDSTs_Moore: $(allDST_Moore_list)
$(allDST_Moore_list): output/%/AllLines_Moore.mdst:
	mkdir -p output/$*
	$(MOORE)/run gaudirun.py Moore_Scripts/$*.py Moore_Scripts/AllLines.py | tee output/$*/AllLines_Moore.out
	rm -f test_catalog.xml

#Once the mDSTs have been produced, we can run a hacked script from upgrade-bandwidth-studies
allEvtSizes_Moore_list=$(foreach MC, $(MC_list),output/$(MC)/AllLines_EvtSize_Moore.txt)
allEvtSizes_Moore: $(allEvtSizes_Moore_list)
$(allEvtSizes_Moore_list): output/%/AllLines_EvtSize_Moore.txt: output/%/AllLines_Moore.mdst
	$(UPGRADE_BANDWIDTH_STUDIES)/run python options/event_size.py $< --path=/Event/HLT2 --banned Sim MC | tee $@


#Time to produce ntuples
alltuple_Moore_list=$(foreach MC, $(MC_list),output/$(MC)/AllLines_Moore.root)
alltuples_Moore: $(alltuple_Moore_list)
$(alltuple_Moore_list): output/%/AllLines_Moore.root: output/%/AllLines_Moore.mdst
	$(DAVINCI)/run gaudirun.py DaVinci_Scripts/$*.py DaVinci_Scripts/AllLines.py

#We have the ntuples, now time to extract the multiplicity of each extra container.
#For each line, we loop over all the containers
#HHGamma
HHGamma_multiplicity_list=$(foreach extra_container, $(extra_container_list), output/HHGamma_${extra_container}_multiplicity.txt)
HHGamma_multiplicities: $(HHGamma_multiplicity_list)
$(HHGamma_multiplicity_list): output/HHGamma_%_multiplicity.txt: $(alltuple_Moore_list) Cuts/%_cuts.txt
	$(ANALYSIS_TOOLS_ROOT)/Multiplicity_Extrasel.out "$(alltuple_Moore_list)" Cuts/$*_cuts.txt $@ HHGammaTuple/DecayTree HHGamma_$*Tuple/DecayTree
#HHGammaEE
HHGammaEE_multiplicity_list=$(foreach extra_container, $(extra_container_list), output/HHGammaEE_${extra_container}_multiplicity.txt)
HHGammaEE_multiplicities: $(HHGammaEE_multiplicity_list)
$(HHGammaEE_multiplicity_list): output/HHGammaEE_%_multiplicity.txt: $(alltuple_Moore_list) Cuts/%_cuts.txt
	$(ANALYSIS_TOOLS_ROOT)/Multiplicity_Extrasel.out "$(alltuple_Moore_list)" Cuts/$*_cuts.txt $@ HHGammaEETuple/DecayTree HHGammaEE_$*Tuple/DecayTree
#HHHGamma
HHHGamma_multiplicity_list=$(foreach extra_container, $(extra_container_list), output/HHHGamma_${extra_container}_multiplicity.txt)
HHHGamma_multiplicities: $(HHHGamma_multiplicity_list)
$(HHHGamma_multiplicity_list): output/HHHGamma_%_multiplicity.txt: $(alltuple_Moore_list) Cuts/%_cuts.txt
	$(ANALYSIS_TOOLS_ROOT)/Multiplicity_Extrasel.out "$(alltuple_Moore_list)" Cuts/$*_cuts.txt $@ HHHGammaTuple/DecayTree HHHGamma_$*Tuple/DecayTree
#HHHGammaEE
HHHGammaEE_multiplicity_list=$(foreach extra_container, $(extra_container_list), output/HHHGammaEE_${extra_container}_multiplicity.txt)
HHHGammaEE_multiplicities: $(HHHGammaEE_multiplicity_list)
$(HHHGammaEE_multiplicity_list): output/HHHGammaEE_%_multiplicity.txt: $(alltuple_Moore_list) Cuts/%_cuts.txt
	$(ANALYSIS_TOOLS_ROOT)/Multiplicity_Extrasel.out "$(alltuple_Moore_list)" Cuts/$*_cuts.txt $@ "HHHGammaEETuple/DecayTree" HHHGammaEE_$*Tuple/DecayTree
#Run all Moore part
all_Moore: HHGamma_multiplicities HHGammaEE_multiplicities HHHGamma_multiplicities HHHGammaEE_multiplicities allEvtSizes_Moore


