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
MC_list_Down=KstG PhiG K1G LambdaG XiG OmegaG PhiKstG PhiPhiG PhiKs0G K1G_KPiPi0 PhiPi0G KstIsoG LambdaPG PhiKG K1G_Cocktail L1520G RhoG
MC_list_Up=XiG OmegaG PhiKstG PhiPhiG PhiKs0G K1G_KPiPi0 PhiPi0G KstIsoG LambdaPG PhiKG K1G_Cocktail L1520G RhoG
MC_list=$(foreach MC, $(MC_list_Down),$(MC)_Down) $(foreach MC, $(MC_list_Up),$(MC)_Up)
#ProdIDs for each MC
KstG_Down_prodID=75829
PhiG_Down_prodID=75812
K1G_Down_prodID=75816
LambdaG_Down_prodID=76702
XiG_Down_prodID=109825
XiG_Up_prodID=109829
OmegaG_Down_prodID=109823
OmegaG_Up_prodID=109827
PhiKstG_Down_prodID=133775
PhiKstG_Up_prodID=133747
PhiPhiG_Down_prodID=133773
PhiPhiG_Up_prodID=133735
PhiKs0G_Down_prodID=133769
PhiKs0G_Up_prodID=133741
K1G_KPiPi0_Down_prodID=133765
K1G_KPiPi0_Up_prodID=133739
PhiPi0G_Down_prodID=133763
PhiPi0G_Up_prodID=133733
KstIsoG_Down_prodID=133761
KstIsoG_Up_prodID=133731
LambdaPG_Down_prodID=133759
LambdaPG_Up_prodID=133727
PhiKG_Down_prodID=133753
PhiKG_Up_prodID=133729
K1G_Cocktail_Down_prodID=133757
K1G_Cocktail_Up_prodID=133723
L1520G_Down_prodID=133755
L1520G_Up_prodID=133721
RhoG_Down_prodID=133751
RhoG_Up_prodID=133725
MinBias_MagDown_prodID=75219

#List of reconstructibles for each MC
KstG_Down_reconstructibles=Kplus,piminus
PhiG_Down_reconstructibles=Kplus,Kminus
K1G_Down_reconstructibles=Kplus,piminus,piplus
LambdaG_Down_reconstructibles=pplus,piminus
XiG_Down_reconstructibles=pplus,piminus,piminus0
XiG_Up_reconstructibles=$(XiG_Down_reconstructibles)
OmegaG_Down_reconstructibles=pplus,piminus,Kminus
OmegaG_Up_reconstructibles=$(OmegaG_Down_reconstructibles)
PhiKstG_Down_reconstructibles=Kplus,Kminus,Kplus0,piminus
PhiKstG_Up_reconstructibles=$(PhiKstG_Down_reconstructibles)
PhiPhiG_Down_reconstructibles=Kplus,Kminus,Kplus0,Kminus0
PhiPhiG_Up_reconstructibles=$(PhiPhiG_Down_reconstructibles)
PhiKs0G_Down_reconstructibles=Kplus,Kminus,piplus,piminus
PhiKs0G_Up_reconstructibles=$(PhiKs0G_Down_reconstructibles)
K1G_KPiPi0_Down_reconstructibles=Kplus,piminus
K1G_KPiPi0_Up_reconstructibles=$(K1G_KPiPi0_Down_reconstructibles)
PhiPi0G_Down_reconstructibles=Kplus,Kminus
PhiPi0G_Up_reconstructibles=$(PhiPi0G_Down_reconstructibles)
KstIsoG_Down_reconstructibles=piplus,piminus,piplus0
KstIsoG_Up_reconstructibles=$(KstIsoG_Down_reconstructibles)
LambdaPG_Down_reconstructibles=pminus,piplus,pplus
LambdaPG_Up_reconstructibles=$(LambdaPG_Down_reconstructibles)
PhiKG_Down_reconstructibles=Kplus,Kminus,Kplus0
PhiKG_Up_reconstructibles=$(PhiKG_Down_reconstructibles)
K1G_Cocktail_Down_reconstructibles=Kplus,piminus,piplus
K1G_Cocktail_Up_reconstructibles=$(K1G_Cocktail_Down_reconstructibles)
L1520G_Down_reconstructibles=pplus,Kminus
L1520G_Up_reconstructibles=$(L1520G_Down_reconstructibles)
RhoG_Down_reconstructibles=piplus,piminus
RhoG_Up_reconstructibles=$(RhoG_Down_reconstructibles)

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
	$(DAVINCI)/run env DECAY=$* gaudirun.py DaVinci_Scripts/Decay_options.py DaVinci_Scripts/AllLines.py DaVinci_Scripts/Input.py

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


