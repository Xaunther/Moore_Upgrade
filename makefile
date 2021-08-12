#Makefile to remember the different commands to run things

#Stack installation
STACKDIR=../stack
MOOREANALYSIS=$(STACKDIR)/MooreAnalysis
MOORE=$(STACKDIR)/Moore
DAVINCI=$(STACKDIR)/DaVinci

#Where folder with root scripts (https://gitlab.cern.ch/aalfonso-Analysis-Tools/root) resides
#Needs compilation before running
ANALYSIS_TOOLS_ROOT=../root

#List of MC samples available
MC_list=KstG PhiG K1G LambdaG XiG OmegaG PhiKstG PhiPhiG PhiKs0G K1G_KPiPi0 PhiPi0G KstIsoG LambdaPG PhiKG K1G_Cocktail L1520G RhoG
#ProdIDs for each MC
KstG_prodID=75829
PhiG_prodID=75812
K1G_prodID=75816
LambdaG_prodID=76702
XiG_prodID=109825
OmegaG_prodID=109823
PhiKstG_prodID=133775
PhiPhiG_prodID=133773
PhiKs0G_prodID=133769
K1G_KPiPi0_prodID=133765
PhiPi0G_prodID=133763
KstIsoG_prodID=133761
LambdaPG_prodID=133759
PhiKG_prodID=133753
K1G_Cocktail_prodID=133757
L1520G_prodID=133755
RhoG_prodID=133751
MinBias_prodID=75219

#List of reconstructibles for each MC
KstG_reconstructibles=Kplus,piminus
PhiG_reconstructibles=Kplus,Kminus
K1G_reconstructibles=Kplus,piminus,piplus
LambdaG_reconstructibles=pplus,piminus
XiG_reconstructibles=pplus,piminus,piminus0
OmegaG_reconstructibles=pplus,piminus,Kminus
PhiKstG_reconstructibles=Kplus,Kminus,Kplus0,piminus
PhiPhiG_reconstructibles=Kplus,Kminus,Kplus0,Kminus0
PhiKs0G_reconstructibles=Kplus,Kminus,piplus,piminus
K1G_KPiPi0_reconstructibles=Kplus,piminus
PhiPi0G_reconstructibles=Kplus,Kminus
KstIsoG_reconstructibles=piplus,piminus,piplus0
LambdaPG_reconstructibles=pminus,piplus,pplus
PhiKG_reconstructibles=Kplus,Kminus,Kplus0
K1G_Cocktail_reconstructibles=Kplus,piminus,piplus
L1520G_reconstructibles=pplus,Kminus
RhoG_reconstructibles=piplus,piminus

#List of extra selection containers
extra_container_list=ExtraHadron ExtraKs0 ExtraLambda ExtraGamma ExtraPi0Merged ExtraPi0Resolved
#List of decaytree keys. Each line has a name for each DecayTree possibility
HHGamma_decay_list=hh hKs0 hL0
HHGammaEE_decay_list=hh hKs0 hL0
HHHGamma_decay_list=hhh hhKs0 hhL0
HHHGammaEE_decay_list=hhh hhKs0 hhL0

#List of important make commands
all: all_MA all_Moore
#Produce efficiencies for all radiative lines and all radiative channels included in MC_list
.PHONY: all_MA
#Produce ntuples with events that pass at least one of a collection of HLT lines (FILTERING)
.PHONY: all_Moore

################################### Input options files ###################################
#Produce input scripts from the ProdIDs (these commands might need rerunning every few months to update PFNs)
.PHONY: input_options_LFNs input_options_PFNs
#This is a prerrequisite for both MooreAnalysis and Moore workflows
#First, get input LFNs from prodID
input_options_LFNs_list=$(foreach MC, $(MC_list),Gaudi_inputs/$(MC)_input_LFNs.py) Gaudi_inputs/MinBias_input_LFNs.py
input_options_LFNs: $(input_options_LFNs_list)
$(input_options_LFNs_list): Gaudi_inputs/%_input_LFNs.py:
	lb-dirac dirac-bookkeeping-get-files --Prod=$($*_prodID) --OptionsFile=$@
#Now translate this list into a PFN list which can be used in Gaudi software.
#Warning (2021/08/05) only works in lxplus, but not in ubuntu + docker
input_options_PFNs_list=$(foreach MC, $(MC_list),Gaudi_inputs/$(MC)_input_PFNs.py) Gaudi_inputs/MinBias_input_PFNs.py
input_options_PFNs: $(input_options_PFNs_list)
$(input_options_PFNs_list): Gaudi_inputs/%_input_PFNs.py: Gaudi_inputs/%_input_LFNs.py
	lb-dirac dirac-bookkeeping-genXMLCatalog --Options=$< --NewOptions=$@

################################### MOORE ANALYSIS PART ###################################
#Produce ntuples from MooreAnalysis.
.PHONY: alltuples_MA alleffs_MA
#They produce MCDecayTreeTuples so all possible events that can be reconstructed with MC matching,
#just FLAGGING whether they pass the HLT lines of interest or not
alltuple_MA_list=$(foreach MC, $(MC_list),output/$(MC)/AllLines_MA.root)
alltuples_MA: $(alltuple_MA_list)
$(alltuple_MA_list): output/%/AllLines_MA.root: Gaudi_inputs/%_input_PFNs.py
	mkdir -p output/$*
	$(MOOREANALYSIS)/run env DECAY=$* gaudirun.py options/Decay_options.py options/2000_Evts.py MooreAnalysis_Scripts/AllLines.py Gaudi_inputs/$*_input_PFNs.py | tee output/$*/AllLines_MA.out

#Produce efficiency results by using the ntuple info
#We use reconstructible children, which only takes children with pseudorapidity in LHCb range
alleff_MA_list=$(foreach MC, $(MC_list),output/$(MC)/AllLines_eff_MA.txt)
alleffs_MA: $(alleff_MA_list)
$(alleff_MA_list): output/%/AllLines_eff_MA.txt: output/%/AllLines_MA.root
	$(MOOREANALYSIS)/run $(MOOREANALYSIS)/HltEfficiencyChecker/scripts/hlt_line_efficiencies.py $< --level Hlt2 --reconstructible-children=$($*_reconstructibles) > $@

#Another thing, get correlation matrices for the 4 trigger lines, in each MC
allcorrelations_MA_list=$(foreach MC, $(MC_list),output/$(MC)/CorrelationMatrix_MA.md)
allcorrelations_MA: $(allcorrelations_MA_list)
$(allcorrelations_MA_list): output/%/CorrelationMatrix_MA.md: output/%/AllLines_MA.root Cuts/HLT2_radiative_cuts.txt
	$(ANALYSIS_TOOLS_ROOT)/CutCorrelation.out $^ $@ MCDecayTreeTuple/MCDecayTree
#Run all Moore Analysis part
all_MA: alleffs_MA allcorrelations_MA

################################### MOORE PART ###################################
#Produce DSTs from Moore.
.PHONY: allDSTs_Moore allEvtSizes_Moore alltuples_Moore
#They produce FILTERED DSTs where only events that pass any HLT line are stored.
allDST_Moore_list=$(foreach MC, $(MC_list),output/$(MC)/AllLines_Moore.mdst) output/MinBias/AllLines_Moore.mdst
allDSTs_Moore: $(allDST_Moore_list)
$(allDST_Moore_list): output/%/AllLines_Moore.mdst: Gaudi_inputs/%_input_PFNs.py
	mkdir -p output/$*
	$(MOORE)/run env DECAY=$* gaudirun.py options/Decay_options.py options/2000_Evts.py Moore_Scripts/AllLines.py Gaudi_inputs/$*_input_PFNs.py | tee output/$*/AllLines_Moore.out
	rm -f test_catalog*.xml

#Once the mDSTs have been produced, we can run a hacked script from upgrade-bandwidth-studies
#Make sure you have prettytable installed
allEvtSizes_Moore_list=$(foreach MC, $(MC_list),output/$(MC)/AllLines_EvtSize_Moore.txt) output/MinBias/AllLines_EvtSize_Moore.txt
allEvtSizes_Moore: $(allEvtSizes_Moore_list)
$(allEvtSizes_Moore_list): output/%/AllLines_EvtSize_Moore.txt: output/%/AllLines_Moore.mdst
	python scripts/event_size.py $< | tee $@


#Time to produce ntuples
alltuple_Moore_list=$(foreach MC, $(MC_list),output/$(MC)/AllLines_Moore.root) output/MinBias/AllLines_Moore.root
alltuples_Moore: $(alltuple_Moore_list)
$(alltuple_Moore_list): output/%/AllLines_Moore.root: output/%/AllLines_Moore.mdst
	$(DAVINCI)/run env DECAY=$* gaudirun.py DaVinci_Scripts/Decay_options.py DaVinci_Scripts/AllLines.py

#We have the ntuples, now time to extract the multiplicity of each extra container.
.PHONY: HHGamma_multiplicities HHGammaEE_multiplicities HHHGamma_multiplicities HHHGammaEE_multiplicities
#For each line, we loop over all the containers
#HHGamma
HHGamma_multiplicity_list=$(foreach extra_container, $(extra_container_list), output/HHGamma_${extra_container}_multiplicity.txt)
HHGamma_multiplicities: $(HHGamma_multiplicity_list)
$(HHGamma_multiplicity_list): output/HHGamma_%_multiplicity.txt: $(alltuple_Moore_list) Cuts/%_cuts.txt
	$(ANALYSIS_TOOLS_ROOT)/Multiplicity_Extrasel.out "$(alltuple_Moore_list)" Cuts/$*_cuts.txt $@ "$(foreach key, $(HHGamma_decay_list),HHGamma_$(key)Tuple/DecayTree)" HHGamma_$*Tuple/DecayTree
#HHGammaEE
HHGammaEE_multiplicity_list=$(foreach extra_container, $(extra_container_list), output/HHGammaEE_${extra_container}_multiplicity.txt)
HHGammaEE_multiplicities: $(HHGammaEE_multiplicity_list)
$(HHGammaEE_multiplicity_list): output/HHGammaEE_%_multiplicity.txt: $(alltuple_Moore_list) Cuts/%_cuts.txt
	$(ANALYSIS_TOOLS_ROOT)/Multiplicity_Extrasel.out "$(alltuple_Moore_list)" Cuts/$*_cuts.txt $@ "$(foreach key, $(HHGammaEE_decay_list),HHGammaEE_$(key)Tuple/DecayTree) HHGammaEE_$*Tuple/DecayTree
#HHHGamma
HHHGamma_multiplicity_list=$(foreach extra_container, $(extra_container_list), output/HHHGamma_${extra_container}_multiplicity.txt)
HHHGamma_multiplicities: $(HHHGamma_multiplicity_list)
$(HHHGamma_multiplicity_list): output/HHHGamma_%_multiplicity.txt: $(alltuple_Moore_list) Cuts/%_cuts.txt
	$(ANALYSIS_TOOLS_ROOT)/Multiplicity_Extrasel.out "$(alltuple_Moore_list)" Cuts/$*_cuts.txt $@ "$(foreach key, $(HHHGamma_decay_list),HHHGamma_$(key)Tuple/DecayTree) HHHGamma_$*Tuple/DecayTree
#HHHGammaEE
HHHGammaEE_multiplicity_list=$(foreach extra_container, $(extra_container_list), output/HHHGammaEE_${extra_container}_multiplicity.txt)
HHHGammaEE_multiplicities: $(HHHGammaEE_multiplicity_list)
$(HHHGammaEE_multiplicity_list): output/HHHGammaEE_%_multiplicity.txt: $(alltuple_Moore_list) Cuts/%_cuts.txt
	$(ANALYSIS_TOOLS_ROOT)/Multiplicity_Extrasel.out "$(alltuple_Moore_list)" Cuts/$*_cuts.txt $@ "$(foreach key, $(HHHGammaEE_decay_list),HHHGammaEE_$(key)Tuple/DecayTree) HHHGammaEE_$*Tuple/DecayTree
#Run all Moore part
all_Moore: HHGamma_multiplicities HHGammaEE_multiplicities HHHGamma_multiplicities HHHGammaEE_multiplicities allEvtSizes_Moore


