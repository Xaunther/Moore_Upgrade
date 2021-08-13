#-- GAUDI jobOptions generated on Fri Aug 13 08:53:17 2021
#-- Contains event types : 
#--   12103202 - 75 files - 78744 events - 298.45 GBytes

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
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000001_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000002_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000003_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000004_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000005_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000006_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000007_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000008_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000009_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000010_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000011_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000012_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000013_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000014_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000015_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000016_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000017_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000018_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000019_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000020_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000021_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000022_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000023_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000024_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000025_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000026_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000027_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000028_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000029_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000030_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000031_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000032_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000033_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000034_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000035_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000036_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000037_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000038_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000039_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000040_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000041_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000042_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000043_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000044_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000045_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000046_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000047_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000048_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000049_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000050_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000051_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000052_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000053_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000054_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000055_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000056_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000057_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000058_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000059_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000060_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000061_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000062_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000063_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000064_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000065_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000066_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000067_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000068_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000069_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000070_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000071_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000072_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000073_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000074_1.xdigi',
'LFN:/lhcb/MC/Upgrade/XDIGI/00133753/0000/00133753_00000075_1.xdigi',
], clear=True)
