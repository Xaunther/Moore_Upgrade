#Makefile to remember the different commands to run things

#Moore installation
MOORE=../stack/Moore
#DaVinci version to use
DAVINCI=lb-run DaVinci/v50r6
#ROOT version to use
ROOT=lb-run ROOT/6.18.04 root -l -b -q
#Gcc compilers
LbLogin8=export BINARY_TAG="x86_64-centos7-gcc8-opt" && export CMTCONFIG="x86_64-centos7-gcc8-opt"
LbLogin9=export BINARY_TAG="x86_64-centos7-gcc9-opt" && export CMTCONFIG="x86_64-centos7-gcc9-opt"
#List of MC samples #PhiG excluded as it is buggy
MC_list=KstG K1G LambdaG

#To Run all 4 lines on different samples. Use default config
default_DST_output_list=$(foreach MC, $(MC_list), output/$(MC)/std_Moore.out)
default_DST_output: $(default_DST_output_list)
$(default_DST_output_list): output/%/std_Moore.out: Moore_Scripts/%.py
	mkdir -p output/$*
	$(LbLogin9) && $(MOORE)/run gaudirun.py Moore_Scripts/$*.py Moore_Scripts/AllLines.py | tee $@
	rm -f test_catalog.xml

#Also, we want to run each line separately, for each MC sample
#HHGamma
default_ntuple_HHGamma_output_list=$(foreach MC, $(MC_list), output/$(MC)/std_DV_HHGamma.out)
default_ntuple_HHGamma_output: $(default_ntuple_HHGamma_output_list)
$(default_ntuple_HHGamma_output_list): output/%/std_DV_HHGamma.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py DaVinci_Scripts/ntuples_HHGamma.py | tee $@
#HHGammaEE
default_ntuple_HHGammaEE_output_list=$(foreach MC, $(MC_list), output/$(MC)/std_DV_HHGammaEE.out)
default_ntuple_HHGammaEE_output: $(default_ntuple_HHGammaEE_output_list)
$(default_ntuple_HHGammaEE_output_list): output/%/std_DV_HHGammaEE.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py DaVinci_Scripts/ntuples_HHGammaEE.py | tee $@
#HHHGamma
default_ntuple_HHHGamma_output_list=$(foreach MC, $(MC_list), output/$(MC)/std_DV_HHHGamma.out)
default_ntuple_HHHGamma_output: $(default_ntuple_HHHGamma_output_list)
$(default_ntuple_HHHGamma_output_list): output/%/std_DV_HHHGamma.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py DaVinci_Scripts/ntuples_HHHGamma.py | tee $@
#HHHGammaEE
default_ntuple_HHHGammaEE_output_list=$(foreach MC, $(MC_list), output/$(MC)/std_DV_HHHGammaEE.out)
default_ntuple_HHHGammaEE_output: $(default_ntuple_HHHGammaEE_output_list)
$(default_ntuple_HHHGammaEE_output_list): output/%/std_DV_HHHGammaEE.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py DaVinci_Scripts/ntuples_HHHGammaEE.py | tee $@
.PHONY: default_ntuple_output
default_ntuple_output: default_ntuple_HHGamma_output default_ntuple_HHGammaEE_output default_ntuple_HHHGamma_output default_ntuple_HHHGammaEE_output

#Another thingy to do here is to clunkily get the average event size
default_DST_size_list=$(foreach MC, $(MC_list), output/$(MC)/evt_size.txt)
default_DST_size: $(default_DST_size_list)
$(default_DST_size_list): output/%/evt_size.txt: output/%/std_Moore.out
	grep "Events output" output/$*/std_Moore.out > $@
	du -sh output/$*/$*.mdst >> $@

########################################## ROOT #######################################
#Once we have the ntuples
#Plot all variables of some relevant ntuple(s)
#HHGamma Line
default_HHGamma_VarList=$(foreach MC, $(MC_list), output/$(MC)/HHGamma_VarList.txt)
default_HHGamma_Var: $(default_HHGamma_VarList)
$(default_HHGamma_VarList): output/%/HHGamma_VarList.txt: output/%/std_DV_HHGamma.out
	$(LbLogin8) && $(ROOT) src/getvars.C\(\"output/$*/$*_HHGamma.root\",\"$@\",\"Hlt2BToHHGamma_Inclusive_Line/DecayTree\"\)
	mkdir -p output/$*/plots/
	mkdir -p output/$*/plots/HHGamma
	../root/PlotUsedVars.out $@ output/$*/$*_HHGamma.root "" E1  output/$*/plots/HHGamma
#Extra hadron
default_ExtraHadron_VarList=$(foreach MC, $(MC_list), output/$(MC)/ExtraHadron_VarList.txt)
default_ExtraHadron_Var: $(default_ExtraHadron_VarList)
$(default_ExtraHadron_VarList): output/%/ExtraHadron_VarList.txt: output/%/std_DV_HHGamma.out
	$(LbLogin8) && $(ROOT) src/getvars.C\(\"output/$*/$*_HHGamma.root\",\"$@\",\"ExtraHadron/DecayTree\"\)
	mkdir -p output/$*/plots/
	mkdir -p output/$*/plots/HHGamma
	mkdir -p output/$*/plots/HHGamma/ExtraHadron
	../root/PlotUsedVars.out $@ output/$*/$*_HHGamma.root "" E1  output/$*/plots/HHGamma/ExtraHadron
#Extra Ks0
default_Ks0_VarList=$(foreach MC, $(MC_list), output/$(MC)/Ks0_VarList.txt)
default_Ks0_Var: $(default_Ks0_VarList)
$(default_Ks0_VarList): output/%/Ks0_VarList.txt: output/%/std_DV_HHGamma.out
	$(LbLogin8) && $(ROOT) src/getvars.C\(\"output/$*/$*_HHGamma.root\",\"$@\",\"ExtraKs0/DecayTree\"\)
	mkdir -p output/$*/plots/
	mkdir -p output/$*/plots/HHGamma
	mkdir -p output/$*/plots/HHGamma/ExtraKs0
	../root/PlotUsedVars.out $@ output/$*/$*_HHGamma.root "" E1  output/$*/plots/HHGamma/ExtraKs0
#Extra Lambda
default_Lambda_VarList=$(foreach MC, $(MC_list), output/$(MC)/Lambda_VarList.txt)
default_Lambda_Var: $(default_Lambda_VarList)
$(default_Lambda_VarList): output/%/Lambda_VarList.txt: output/%/std_DV_HHGamma.out
	$(LbLogin8) && $(ROOT) src/getvars.C\(\"output/$*/$*_HHGamma.root\",\"$@\",\"ExtraLambda/DecayTree\"\)
	mkdir -p output/$*/plots/
	mkdir -p output/$*/plots/HHGamma
	mkdir -p output/$*/plots/HHGamma/ExtraLambda
	../root/PlotUsedVars.out $@ output/$*/$*_HHGamma.root "" E1  output/$*/plots/HHGamma/ExtraLambda

#Efficiency of extracuts
#Hadron
default_HHGamma_extraHadronCutEff_list=$(foreach MC, $(MC_list), output/$(MC)/HHGamma_extraHadronCutEff.txt)
default_HHGamma_extraHadronCutEff: $(default_HHGamma_extraHadronCutEff_list)
$(default_HHGamma_extraHadronCutEff_list): output/%/HHGamma_extraHadronCutEff.txt: output/%/std_DV_HHGamma.out Cuts/extraHadroncuts.txt
	../root/CutEff.out output/$*/$*_HHGamma.root Cuts/extraHadroncuts.txt "" $@ "" ExtraHadron/DecayTree
#Ks0
default_HHGamma_extraKs0CutEff_list=$(foreach MC, $(MC_list), output/$(MC)/HHGamma_extraKs0CutEff.txt)
default_HHGamma_extraKs0CutEff: $(default_HHGamma_extraKs0CutEff_list)
$(default_HHGamma_extraKs0CutEff_list): output/%/HHGamma_extraKs0CutEff.txt: output/%/std_DV_HHGamma.out Cuts/extraKs0cuts.txt
	../root/CutEff.out output/$*/$*_HHGamma.root Cuts/extraKs0cuts.txt "" $@ "" ExtraKs0/DecayTree
#Lambda
default_HHGamma_extraLambdaCutEff_list=$(foreach MC, $(MC_list), output/$(MC)/HHGamma_extraLambdaCutEff.txt)
default_HHGamma_extraLambdaCutEff: $(default_HHGamma_extraLambdaCutEff_list)
$(default_HHGamma_extraLambdaCutEff_list): output/%/HHGamma_extraLambdaCutEff.txt: output/%/std_DV_HHGamma.out Cuts/extraLambdacuts.txt
	../root/CutEff.out output/$*/$*_HHGamma.root Cuts/extraLambdacuts.txt "" $@ "" ExtraLambda/DecayTree

#Run all default stuff
.PHONY: all_default
all_default: default_ntuple_output default_DST_size default_HHGamma_Var default_ExtraHadron_Var default_Ks0_Var default_HHGamma_extraHadronCutEff default_HHGamma_extraKs0CutEff default_HHGamma_extraLambdaCutEff
