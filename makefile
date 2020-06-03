#Makefile to remember the different commands to run things

#Moore installation
MOORE=../stack/Moore
#Gcc compilers
LbLogin8=export BINARY_TAG="x86_64-centos7-gcc8-opt" && export CMTCONFIG="x86_64-centos7-gcc8-opt"
LbLogin9=export BINARY_TAG="x86_64-centos7-gcc9-opt" && export CMTCONFIG="x86_64-centos7-gcc9-opt"

#To Run all 4 lines on different samples. Use default config
default_DST_output_list=output/KstG/std.out output/K1G/std.out output/PhiG/std.out output/LambdaG/std.out
default_DST_output: $(default_DST_output_list)
$(default_DST_output_list): output/%/std.out: Moore_Scripts/%.py
	$(LbLogin9) && $(MOORE)/run gaudirun.py Moore_Scripts/$*.py Moore_Scripts/AllLines.py | tee $*.out
	mv $*.out $@
	rm -f test_catalog.xml
