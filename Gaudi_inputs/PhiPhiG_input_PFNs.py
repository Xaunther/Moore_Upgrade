#-- GAUDI jobOptions generated on Wed Aug  4 17:09:36 2021
#-- Contains event types : 
#--   13104212 - 54 files - 52992 events - 199.75 GBytes

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
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133773/0000/00133773_00000001_1.xdigi',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000002_1.xdigi',
'root://lhcb-sdpd7.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000003_1.xdigi',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000004_1.xdigi',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000005_1.xdigi',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000006_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133773/0000/00133773_00000007_1.xdigi',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000008_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000009_1.xdigi',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000010_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000011_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133773/0000/00133773_00000012_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000013_1.xdigi',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000014_1.xdigi',
'root://lhcbsdrm.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000015_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000016_1.xdigi',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000017_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000018_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000019_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000020_1.xdigi',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000021_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000022_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133773/0000/00133773_00000023_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000024_1.xdigi',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000025_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000026_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000027_1.xdigi',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000028_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000029_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000030_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133773/0000/00133773_00000031_1.xdigi',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000032_1.xdigi',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000033_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000034_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000035_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000036_1.xdigi',
'root://lhcbsdrm.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000037_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000038_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000039_1.xdigi',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000040_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133773/0000/00133773_00000041_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000042_1.xdigi',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000043_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000044_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000045_1.xdigi',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000046_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133773/0000/00133773_00000047_1.xdigi',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000048_1.xdigi',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000049_1.xdigi',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000050_1.xdigi',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000051_1.xdigi',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000052_1.xdigi',
'root://lhcb-sdpd8.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000053_1.xdigi',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133773/0000/00133773_00000054_1.xdigi',
], clear=True)
