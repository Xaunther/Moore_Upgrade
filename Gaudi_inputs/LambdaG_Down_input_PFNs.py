#-- GAUDI jobOptions generated on Fri Aug 13 08:53:10 2021
#-- Contains event types : 
#--   15102307 - 54 files - 47102 events - 32.68 GBytes

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
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000001_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000002_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000003_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000004_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000005_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000006_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000007_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000008_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000009_1.ldst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/LDST/00076702/0000/00076702_00000010_1.ldst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/LDST/00076702/0000/00076702_00000011_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000012_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000013_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000014_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000016_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000018_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000019_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000020_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000021_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000022_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000023_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000024_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000025_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000026_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000027_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000028_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000029_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000030_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000031_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000032_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000033_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000035_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000036_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000037_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000038_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000039_1.ldst',
'root://lhcb-sdpd11.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000040_1.ldst',
'root://lhcb-sdpd8.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000041_1.ldst',
'root://x509up_u1000@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000042_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000046_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000049_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000050_1.ldst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/LDST/00076702/0000/00076702_00000051_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000052_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000054_1.ldst',
'root://x509up_u1000@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000056_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000057_1.ldst',
'root://x509up_u1000@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000058_1.ldst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/LDST/00076702/0000/00076702_00000059_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000062_1.ldst',
'root://lhcb-sdpd8.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000063_1.ldst',
'root://x509up_u1000@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000064_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000070_1.ldst',
'root://x509up_u1000@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00076702/0000/00076702_00000072_1.ldst',
], clear=True)
