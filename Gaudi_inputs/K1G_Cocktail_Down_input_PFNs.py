#-- GAUDI jobOptions generated on Fri Aug 13 08:53:16 2021
#-- Contains event types : 
#--   12203271 - 58 files - 61452 events - 231.59 GBytes

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
'root://x509up_u1000@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000001_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000002_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133757/0000/00133757_00000003_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133757/0000/00133757_00000004_1.xdigi',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000005_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133757/0000/00133757_00000006_1.xdigi',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000007_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000008_1.xdigi',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000009_1.xdigi',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000010_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000011_1.xdigi',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000012_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000013_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133757/0000/00133757_00000014_1.xdigi',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000015_1.xdigi',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000016_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000017_1.xdigi',
'root://x509up_u1000@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000018_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000019_1.xdigi',
'root://x509up_u1000@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000020_1.xdigi',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000021_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000022_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000023_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000024_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000025_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000026_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000027_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000028_1.xdigi',
'root://lhcb-sespd1.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000029_1.xdigi',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000030_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000031_1.xdigi',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000032_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133757/0000/00133757_00000033_1.xdigi',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000034_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000035_1.xdigi',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000036_1.xdigi',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000037_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133757/0000/00133757_00000038_1.xdigi',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000039_1.xdigi',
'root://x509up_u1000@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000040_1.xdigi',
'root://x509up_u1000@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000041_1.xdigi',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000042_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000043_1.xdigi',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDIGI/00133757/0000/00133757_00000044_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000045_1.xdigi',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000046_1.xdigi',
'root://x509up_u1000@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000047_1.xdigi',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000048_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000049_1.xdigi',
'root://lhcb-sdpd13.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000050_1.xdigi',
'root://x509up_u1000@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000052_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000053_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000054_1.xdigi',
'root://x509up_u1000@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000055_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000056_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000057_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000058_1.xdigi',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDIGI/00133757/0000/00133757_00000059_1.xdigi',
], clear=True)
