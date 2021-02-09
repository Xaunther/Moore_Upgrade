#-- GAUDI jobOptions generated on Tue Feb  9 11:19:11 2021
#-- Contains event types : 
#--   11102202 - 29 files - 102963 events - 65.50 GBytes

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
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000023_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000016_1.ldst',
'root://lhcb-sdpd7.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000029_1.ldst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000032_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000021_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000012_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000011_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000010_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000007_1.ldst',
'root://x509up_u98003@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000020_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000015_1.ldst',
'root://lhcb-sdpd11.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000024_1.ldst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/LDST/00075829/0000/00075829_00000031_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000017_1.ldst',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000034_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000008_1.ldst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000005_1.ldst',
'root://x509up_u98003@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000025_1.ldst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000001_1.ldst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000003_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000028_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000014_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000013_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000009_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000018_1.ldst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/LDST/00075829/0000/00075829_00000026_1.ldst',
'root://x509up_u98003@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000022_1.ldst',
'root://x509up_u98003@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000019_1.ldst',
'root://x509up_u98003@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075829/0000/00075829_00000004_1.ldst',
], clear=True)
