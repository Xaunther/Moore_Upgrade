#-- GAUDI jobOptions generated on Tue Feb  9 11:24:14 2021
#-- Contains event types : 
#--   16103332 - 163 files - 201977 events - 700.05 GBytes

#--  Extra information about the data processing phases:

#--  Processing Pass: 'Step-141795' 

#--  StepId : 141795 
#--  StepName : Digi15-Upgrade for Upgrade studies with spillover - 2017 Baseline NoRichSpillover - xdigi 
#--  ApplicationName : Boole 
#--  ApplicationVersion : v40r6 
#--  OptionFiles : $APPCONFIGOPTS/Boole/Default.py;$APPCONFIGOPTS/Boole/Boole-Upgrade-Baseline-20150522.py;$APPCONFIGOPTS/Boole/EnableSpillover.py;$APPCONFIGOPTS/Boole/Upgrade-RichMaPMT-NoSpilloverDigi.py;$APPCONFIGOPTS/Boole/xdigi.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r395 
#--  Visible : N 

#--  Processing Pass: 'Step-141796' 

#--  StepId : 141796 
#--  StepName : Reco-Up03 for Upgrade studies - 2017 Baseline Geometry - XDST 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v61r0 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Brunel/Brunel-Upgrade-Baseline-20150522.py;$APPCONFIGOPTS/Brunel/patchUpgrade1.py;$APPCONFIGOPTS/Brunel/xdst.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r395 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles([
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000051_2.xdst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000005_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000011_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000150_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000070_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000139_2.xdst',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000100_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000123_2.xdst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000104_2.xdst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000112_2.xdst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDST/00109823/0000/00109823_00000102_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000019_2.xdst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDST/00109823/0000/00109823_00000001_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000050_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000084_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000062_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000021_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000125_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000083_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000044_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000080_2.xdst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000107_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000113_2.xdst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000024_2.xdst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000163_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000099_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000030_2.xdst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDST/00109823/0000/00109823_00000116_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000022_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000032_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000117_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000029_2.xdst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000097_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000081_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000075_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000015_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000085_2.xdst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000141_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000090_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000153_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000057_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000087_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000098_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000037_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000110_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000053_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000060_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000045_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000026_2.xdst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000159_2.xdst',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000041_2.xdst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000134_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000047_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000108_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000036_2.xdst',
'root://lhcb-sdpd23.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000120_2.xdst',
'root://lhcb-sdpd24.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000007_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000020_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000096_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000071_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000069_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000082_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000144_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000094_2.xdst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000146_2.xdst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000155_2.xdst',
'root://lhcb-sdpd6.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000154_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000042_2.xdst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000135_2.xdst',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000002_2.xdst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000151_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000119_2.xdst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000140_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000105_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000077_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000039_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000052_2.xdst',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000004_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000018_2.xdst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDST/00109823/0000/00109823_00000165_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000038_2.xdst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000160_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000079_2.xdst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000115_2.xdst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000058_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000074_2.xdst',
'root://lhcbsdrm.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000031_2.xdst',
'root://lhcb-sdpd16.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000076_2.xdst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000142_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000064_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000049_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000114_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000035_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000130_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000017_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000055_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000122_2.xdst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000145_2.xdst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000006_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000078_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000068_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000089_2.xdst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000008_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000127_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000072_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000073_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000129_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000028_2.xdst',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000016_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000131_2.xdst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000126_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000040_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000013_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000034_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000103_2.xdst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000012_2.xdst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000106_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000133_2.xdst',
'root://lhcb-sdpd6.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000137_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000059_2.xdst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDST/00109823/0000/00109823_00000066_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000093_2.xdst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000111_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000023_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000132_2.xdst',
'root://lhcb-sdpd16.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000118_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000086_2.xdst',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000157_2.xdst',
'root://lhcb-sdpd16.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000166_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000009_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000109_2.xdst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000162_2.xdst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000164_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000033_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000027_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000149_2.xdst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDST/00109823/0000/00109823_00000003_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000092_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000088_2.xdst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000124_2.xdst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDST/00109823/0000/00109823_00000138_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000063_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000101_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000061_2.xdst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000128_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000161_2.xdst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/XDST/00109823/0000/00109823_00000121_2.xdst',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000095_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000067_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000056_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000167_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000048_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000054_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000046_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000043_2.xdst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000010_2.xdst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000152_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000014_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000136_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000148_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000091_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000065_2.xdst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/XDST/00109823/0000/00109823_00000143_2.xdst',
], clear=True)
