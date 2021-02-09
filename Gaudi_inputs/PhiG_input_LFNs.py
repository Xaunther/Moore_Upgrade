#-- GAUDI jobOptions generated on Tue Feb  9 11:19:43 2021
#-- Contains event types : 
#--   13102202 - 35 files - 98901 events - 59.68 GBytes

#--  Extra information about the data processing phases:

#--  Processing Pass: 'Step-133571' 

#--  StepId : 133571 
#--  StepName : TCK-0x52000000 (HLT1) Filter upgrade samples - LDST 
#--  ApplicationName : Moore 
#--  ApplicationVersion : v30r0 
#--  OptionFiles : $APPCONFIGOPTS/Moore/MooreSimFilteringForUpgrade.py;$APPCONFIGOPTS/Conditions/TCK-0x52000000.py;$APPCONFIGOPTS/Moore/DataType-Upgrade.py;$APPCONFIGOPTS/Moore/MooreSimProductionHlt1.py;$APPCONFIGOPTS/Moore/ReadSplitRawEvent.py 
#--  DDDB : dddb-20171126 
#--  CONDDB : sim-20171127-vc-md100 
#--  ExtraPackages : AppConfig.v3r358 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles([
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000002_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000049_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000006_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000031_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000017_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000013_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000012_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000041_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000028_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000036_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000018_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000040_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000005_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000007_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000010_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000046_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000011_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000055_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000015_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000008_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000004_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000026_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000045_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000057_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000042_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000001_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000027_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000052_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000037_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000043_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000047_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000053_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000016_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000014_1.ldst',
'LFN:/lhcb/MC/Upgrade/LDST/00075812/0000/00075812_00000033_1.ldst',
], clear=True)
