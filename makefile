#Makefile to remember the different commands to run things

#Moore installation
MOORE=../stack/Moore
#DaVinci version to use
DAVINCI=lb-run DaVinci/v50r6
#Gcc compilers
LbLogin8=export BINARY_TAG="x86_64-centos7-gcc8-opt" && export CMTCONFIG="x86_64-centos7-gcc8-opt"
LbLogin9=export BINARY_TAG="x86_64-centos7-gcc9-opt" && export CMTCONFIG="x86_64-centos7-gcc9-opt"

#To Run all 4 lines on different samples. Use default config
default_DST_output_list=output/KstG/std_Moore.out output/K1G/std_Moore.out output/PhiG/std_Moore.out output/LambdaG/std_Moore.out
default_DST_output: $(default_DST_output_list)
$(default_DST_output_list): output/%/std_Moore.out: Moore_Scripts/%.py
	mkdir -p output/$*
	$(LbLogin9) && $(MOORE)/run gaudirun.py Moore_Scripts/$*.py Moore_Scripts/AllLines.py | tee $@
	rm -f test_catalog.xml

#Also, we want to run each line separately, for each MC sample
#HHGamma
default_ntuple_HHGamma_output_list=output/KstG/std_DV_HHGamma.out output/K1G/std_DV_HHGamma.out output/PhiG/std_DV_HHGamma.out output/LambdaG/std_DV_HHGamma.out
default_ntuple_HHGamma_output: $(default_ntuple_HHGamma_output_list)
$(default_ntuple_HHGamma_output_list): output/%/std_DV_HHGamma.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py DaVinci_Scripts/ntuples_HHGamma.py | tee $@
#HHGammaEE
default_ntuple_HHGammaEE_output_list=output/KstG/std_DV_HHGammaEE.out output/K1G/std_DV_HHGammaEE.out output/PhiG/std_DV_HHGammaEE.out output/LambdaG/std_DV_HHGammaEE.out
default_ntuple_HHGammaEE_output: $(default_ntuple_HHGammaEE_output_list)
$(default_ntuple_HHGammaEE_output_list): output/%/std_DV_HHGammaEE.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py DaVinci_Scripts/ntuples_HHGammaEE.py | tee $@
#HHHGamma
default_ntuple_HHHGamma_output_list=output/KstG/std_DV_HHHGamma.out output/K1G/std_DV_HHHGamma.out output/PhiG/std_DV_HHHGamma.out output/LambdaG/std_DV_HHHGamma.out
default_ntuple_HHHGamma_output: $(default_ntuple_HHHGamma_output_list)
$(default_ntuple_HHHGamma_output_list): output/%/std_DV_HHHGamma.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py DaVinci_Scripts/ntuples_HHHGamma.py | tee $@
#HHHGammaEE
default_ntuple_HHHGammaEE_output_list=output/KstG/std_DV_HHHGammaEE.out output/K1G/std_DV_HHHGammaEE.out output/PhiG/std_DV_HHHGammaEE.out output/LambdaG/std_DV_HHHGammaEE.out
default_ntuple_HHHGammaEE_output: $(default_ntuple_HHHGammaEE_output_list)
$(default_ntuple_HHHGammaEE_output_list): output/%/std_DV_HHHGammaEE.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py DaVinci_Scripts/ntuples_HHHGammaEE.py | tee $@
.PHONY: default_ntuple_output
default_ntuple_output: default_ntuple_HHGamma_output default_ntuple_HHGammaEE_output default_ntuple_HHHGamma_output default_ntuple_HHHGammaEE_output

#Another thingy to do here is to clunkily get the average event size
default_DST_size_list=output/KstG/evt_size.txt output/PhiG/evt_size.txt output/LambdaG/evt_size.txt output/K1G/evt_size.txt
default_DST_size: $(default_DST_size_list)
$(default_DST_size_list): output/%/evt_size.txt: output/%/std_Moore.out
	grep "Events output" output/$*/std_Moore.out > $@
	du -sh output/$*/$*.mdst >> $@

#Run all default stuff
.PHONY: all_default
all_default: default_ntuple_output default_DST_size
