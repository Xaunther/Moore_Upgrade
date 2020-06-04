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
	$(LbLogin9) && $(MOORE)/run gaudirun.py Moore_Scripts/$*.py Moore_Scripts/AllLines.py | tee $*_Moore.out
	mv $*_Moore.out $@
	rm -f test_catalog.xml

#Also, we want to run each line separately, for each MC sample
#HHGamma
default_ntuple_HHGamma_output_list=output/KstG/std_DV_HHGamma.out output/K1G/std_DV_HHGamma.out output/PhiG/std_DV_HHGamma.out output/LambdaG/std_DV_HHGamma.out
default_ntuple_HHGamma_output: $(default_ntuple_HHGamma_output_list)
$(default_ntuple_HHGamma_output_list): output/%/std_DV_HHGamma.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py Moore_Scripts/ntuples_HHGamma.py | tee $*_DV_HHGamma.out
	mv $*_DV_HHGamma.out $@
#HHGammaEE
default_ntuple_HHGammaEE_output_list=output/KstG/std_DV_HHGammaEE.out output/K1G/std_DV_HHGammaEE.out output/PhiG/std_DV_HHGammaEE.out output/LambdaG/std_DV_HHGammaEE.out
default_ntuple_HHGammaEE_output: $(default_ntuple_HHGammaEE_output_list)
$(default_ntuple_HHGammaEE_output_list): output/%/std_DV_HHGammaEE.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py Moore_Scripts/ntuples_HHGammaEE.py | tee $*_DV_HHGammaEE.out
	mv $*_DV_HHGammaEE.out $@
#HHHGamma
default_ntuple_HHHGamma_output_list=output/KstG/std_DV_HHHGamma.out output/K1G/std_DV_HHHGamma.out output/PhiG/std_DV_HHHGamma.out output/LambdaG/std_DV_HHHGamma.out
default_ntuple_HHHGamma_output: $(default_ntuple_HHHGamma_output_list)
$(default_ntuple_HHHGamma_output_list): output/%/std_DV_HHHGamma.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py Moore_Scripts/ntuples_HHHGamma.py | tee $*_DV_HHHGamma.out
	mv $*_DV_HHHGamma.out $@
#HHHGammaEE
default_ntuple_HHHGammaEE_output_list=output/KstG/std_DV_HHHGammaEE.out output/K1G/std_DV_HHHGammaEE.out output/PhiG/std_DV_HHHGammaEE.out output/LambdaG/std_DV_HHHGammaEE.out
default_ntuple_HHHGammaEE_output: $(default_ntuple_HHHGammaEE_output_list)
$(default_ntuple_HHHGammaEE_output_list): output/%/std_DV_HHHGammaEE.out: output/%/std_Moore.out
	$(LbLogin9) && $(DAVINCI) gaudirun.py DaVinci_Scripts/$*.py Moore_Scripts/ntuples_HHHGammaEE.py | tee $*_DV_HHHGammaEE.out
	mv $*_DV_HHHGammaEE.out $@
.PHONY: default_ntuple_output
default_ntuple_output: default_ntuple_HHGamma_output default_ntuple_HHGammaEE_output default_ntuple_HHHGamma_output default_ntuple_HHHGammaEE_output
