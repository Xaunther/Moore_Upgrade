#Makefile to remember the different commands to run things

#Moore installation
MOORE=../stack/Moore

#To Run all 4 lines on different samples. Use default config
default_DST_output_list=output/KstG/std.out output/K1G/std.out output/PhiG/std.out output/LambdaG/std.out
default_DST_output: $(default_DST_output_list)
$(default_DST_output_list): output/%/std.out: Moore_Scripts/%.py
	$(MOORE)/run gaudirun.py Moore_Scripts$*.py Moore_Scripts/AllLines.py | tee $*.out
	mv $*.out $@
	rm -f test_catalog.xml
