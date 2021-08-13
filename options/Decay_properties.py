#Dictionary with properties of the MC needed to run Moore, DaVinci, MooreAnalysis.
#Reco from file switch. To turn it on/off for all MC that can be switched off
#For the others (XDIGI) it has to be on always
reco_from_file = True

props = {
    "KstG": {
        'descriptor':
        "[${B0}B0 -> ${Kst_892_0}(K*(892)0 -> ${Kplus}K+ ${piminus}pi-) gamma]CC",
        'evtnumber':
        "11102202",
        'dddb_tag':
        "dddb-20171126",
        'conddb_tag':
        "sim-20171127-vc-m{0}100",
        'input_raw_format':
        4.3,
        'reco_from_file':
        reco_from_file,
        'ft_decoding_version':
        2,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim09c-Up02/Reco-Up01/Trig0x52000000/11102202/LDST"
    },
    "PhiG": {
        'descriptor':
        "[${B_s0}B_s0 -> (phi(1020) -> ${Kplus}K+ ${Kminus}K-) gamma]CC",
        'evtnumber':
        "13102202",
        'dddb_tag':
        "dddb-20171126",
        'conddb_tag':
        "sim-20171127-vc-m{0}100",
        'input_raw_format':
        4.3,
        'reco_from_file':
        reco_from_file,
        'ft_decoding_version':
        2,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim09c-Up02/Reco-Up01/Trig0x52000000/13102202/LDST"
    },
    "K1G": {
        'descriptor':
        "[${Bplus}B+ -> (K_1(1270)+ --> ${Kplus}K+ ${piminus}pi- ${piplus}pi+) gamma]CC",
        'evtnumber':
        "12203224",
        'dddb_tag':
        "dddb-20171126",
        'conddb_tag':
        "sim-20171127-vc-m{0}100",
        'input_raw_format':
        4.3,
        'reco_from_file':
        reco_from_file,
        'ft_decoding_version':
        2,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim09c-Up02/Reco-Up01/Trig0x52000000/12203224/LDST"
    },
    "LambdaG": {
        'descriptor':
        "[${Lamdba_b0}Lambda_b0 -> (Lambda0 -> ${pplus}p+ ${piminus}pi-) gamma]CC",
        'evtnumber':
        "15102307",
        'dddb_tag':
        "dddb-20171126",
        'conddb_tag':
        "sim-20171127-vc-m{0}100",
        'input_raw_format':
        4.3,
        'reco_from_file':
        reco_from_file,
        'ft_decoding_version':
        2,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim09c-Up02/Reco-Up01/Trig0x52000000/15102307/LDST"
    },
    "XiG": {
        'descriptor':
        "[${Xi_b}Xi_b- -> (Xi- ->(Lambda0 -> ${pplus}p+ ${piminus}pi-) ${piminus0}pi-) gamma]CC",
        'evtnumber':
        "16103330",
        'dddb_tag':
        "dddb-20190223",
        'conddb_tag':
        "sim-20180530-vc-m{0}100",
        'input_raw_format':
        4.3,
        'reco_from_file':
        reco_from_file,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up05/Reco-Up03/16103330/XDST"
    },
    "OmegaG": {
        'descriptor':
        "[${Omega_b}Xi_b- -> (Omega- ->(Lambda0 -> ${pplus}p+ ${piminus}pi-) ${Kminus}K- ) gamma]CC",
        'evtnumber':
        "16103332",
        'dddb_tag':
        "dddb-20190223",
        'conddb_tag':
        "sim-20180530-vc-m{0}100",
        'input_raw_format':
        4.3,
        'reco_from_file':
        reco_from_file,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up05/Reco-Up03/16103332/XDST"
    },
    "PhiKstG": {
        'descriptor':
        "[${B0}B0 -> (phi(1020) -> ${Kplus}K+ ${Kminus}K-) (K*(892)0 -> ${Kplus0}K+ ${piminus}pi-) gamma]CC",
        'evtnumber':
        "11104202",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/11104202/XDIGI"
    },
    "PhiPhiG": {
        'descriptor':
        "[${B0}B_s0 -> (phi(1020) -> ${Kplus}K+ ${Kminus}K-) (phi(1020) -> ${Kplus0}K+ ${Kminus0}K-) gamma]CC",
        'evtnumber':
        "13104212",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/13104212/XDIGI"
    },
    "PhiKs0G": {
        'descriptor':
        "[${B0}Beauty -> (phi(1020) -> ${Kplus}K+ ${Kminus}K-) (KS0 -> ${piplus}pi+ ${piminus}pi-) gamma]CC",
        'evtnumber':
        "11104372",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/11104372/XDIGI"
    },
    "K1G_KPiPi0": {
        'descriptor':
        "[${B0}B0 -> ${K1_1270_0}(K_1(1270)0 -> (X0 -> ${Kplus}K+ ${piminus}pi- pi0)) gamma]CC",
        'evtnumber':
        "11202603",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/11202603/XDIGI"
    },
    "PhiPi0G": {
        'descriptor':
        "[${B0}B_s0 -> (phi(1020) -> ${Kplus}K+ ${Kminus}K-) pi0 gamma]CC",
        'evtnumber':
        "13102212",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/13102212/XDIGI"
    },
    "KstIsoG": {
        'descriptor':
        "[${Bplus}B+ -> ${Kst_plus}(K*(892)+ -> ${KS0}(KS0 -> ${piplus}pi+ ${piminus}pi-) ${piplus0}pi+) gamma]CC",
        'evtnumber':
        "12203303",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/12203303/XDIGI"
    },
    "LambdaPG": {
        'descriptor':
        "[${Bplus}B+ -> ${Lambda_0}(Lambda~0 -> ${pminus}p~- ${piplus}pi+) ${pplus}p+ gamma]CC",
        'evtnumber':
        "12103331",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/12103331/XDIGI"
    },
    "PhiKG": {
        'descriptor':
        "[${Bplus}B+ -> (phi(1020) -> ${Kplus}K+ ${Kminus}K-) ${Kplus0}K+ gamma]CC",
        'evtnumber':
        "12103202",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/12103202/XDIGI"
    },
    "K1G_Cocktail": {
        'descriptor':
        "[${Bplus}B+ -> ${K1_plus}(K_1(1270)+ -> (X -> ${Kplus}K+ ${piminus}pi- ${piplus}pi+)) gamma ]CC",
        'evtnumber':
        "12203271",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/12203271/XDIGI"
    },
    "L1520G": {
        'descriptor':
        "[${Lambda_b0}Lambda_b0 -> ${Lambda_1520_0}(Lambda(1520)0 -> ${pplus}p+ ${Kminus}K-) gamma]CC",
        'evtnumber':
        "15102203",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/15102203/XDIGI"
    },
    "RhoG": {
        'descriptor':
        "[${B0}B0 -> (rho(770)0 -> ${piplus}pi+ ${piminus}pi-) gamma]CC",
        'evtnumber':
        "11102222",
        'dddb_tag':
        "dddb-20210218",
        'conddb_tag':
        "sim-20201218-vc-m{0}100",
        'input_raw_format':
        0.3,
        'reco_from_file':
        False,
        'ft_decoding_version':
        6,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim10-Up08/Digi15-Up04/11102222/XDIGI"
    },
    "MinBias": {
        'evtnumber':
        "30000000",
        'dddb_tag':
        "dddb-20171126 ",
        'conddb_tag':
        "sim-20171127-vc-m{0}100",
        'input_raw_format':
        4.3,
        'reco_from_file':
        reco_from_file,
        'ft_decoding_version':
        2,
        'dirac-path':
        "/MC/Upgrade/Beam7000GeV-Upgrade-Mag{0}-Nu7.6-25ns-Pythia8/Sim09c-Up02/Reco-Up01/Trig0x52000000/30000000/LDST"
    }
}