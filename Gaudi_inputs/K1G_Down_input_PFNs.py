#-- GAUDI jobOptions generated on Fri Aug 13 08:53:09 2021
#-- Contains event types : 
#--   12203224 - 39 files - 101929 events - 65.08 GBytes

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
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000001_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000002_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000003_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000004_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000005_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000006_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000007_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000008_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000009_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000010_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000012_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000013_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000015_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000016_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000017_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000018_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000022_1.ldst',
'root://x509up_u1000@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000025_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000026_1.ldst',
'root://lhcb-sdpd3.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000027_1.ldst',
'root://x509up_u1000@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000028_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000029_1.ldst',
'root://x509up_u1000@eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000033_1.ldst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/LDST/00075816/0000/00075816_00000034_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000035_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000037_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000039_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000041_1.ldst',
'root://xrootd.echo.stfc.ac.uk/lhcb:prod/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000042_1.ldst',
'root://lhcb-sdpd3.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000043_1.ldst',
'root://xrootd-lhcb.cr.cnaf.infn.it:1094//storage/gpfs_lhcb/lhcb/disk/MC/Upgrade/LDST/00075816/0000/00075816_00000048_1.ldst',
'root://x509up_u1000@lhcbxrootd-kit.gridka.de//pnfs/gridka.de/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000049_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000052_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000053_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000054_1.ldst',
'root://x509up_u1000@ccxrootdlhcb.in2p3.fr//pnfs/in2p3.fr/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000055_1.ldst',
'root://x509up_u1000@xrootd.pic.es//pnfs/pic.es/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000056_1.ldst',
'root://lhcb-sdpd7.t1.grid.kiae.ru:1094/t1.grid.kiae.ru/data/lhcb/lhcbdisk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000057_1.ldst',
'root://x509up_u1000@xrootd.grid.surfsara.nl//pnfs/grid.sara.nl/data/lhcb/LHCb-Disk/lhcb/MC/Upgrade/LDST/00075816/0000/00075816_00000058_1.ldst',
], clear=True)
