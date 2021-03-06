#-- GAUDI jobOptions generated on Fri Aug 13 08:53:29 2021
#-- Contains event types : 
#--   12103331 - 62 files - 64545 events - 245.07 GBytes

#--  Extra information about the data processing phases:

#--  Processing Pass: 'Step-146329' 

#--  StepId : 146329 
#--  StepName : Digi15-Upgrade for Upgrade studies with spillover - 2017 Baseline NoRichSpillover - xdigi 
#--  ApplicationName : Boole 
#--  ApplicationVersion : v41r3 
#--  OptionFiles : $APPCONFIGOPTS/Boole/Default.py;$APPCONFIGOPTS/Boole/EnableSpillover.py;$APPCONFIGOPTS/Boole/Boole-Upgrade-Baseline-20200616.py;$APPCONFIGOPTS/Boole/Upgrade-RichMaPMT-NoSpilloverDigi.py;$APPCONFIGOPTS/Boole/xdigi.py;$APPCONFIGOPTS/Boole/Boole-Upgrade-IntegratedLumi.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r403 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles([
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000001_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000002_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000003_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000004_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000005_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000006_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000007_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000008_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000009_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000010_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000011_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000012_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000013_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000014_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000015_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000016_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000017_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000018_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000019_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000020_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000021_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000022_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000023_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000024_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000025_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000026_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000027_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000028_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000029_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000030_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000031_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000032_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000033_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000034_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000035_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000036_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000037_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000038_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000039_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000040_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000041_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000042_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000043_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000045_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000046_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000047_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000048_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000049_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000050_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000051_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000052_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000053_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000054_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000055_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000056_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000057_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000058_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000059_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000060_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000061_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000062_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133727/0000/00133727_00000063_1.xdigi',
], clear=True)
