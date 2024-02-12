import ROOT

# global parameters
intLumi = 5.0e06  # in pb-1
ana_tex = "e^{+}e^{-} #rightarrow ZH #rightarrow #nu#bar{#nu} + X"
delphesVersion = "3.4.2"
energy = 240.0
collider = "FCC-ee"
BES = False
inputDir = "/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZnunuHqq/finalsel/"
formats = ["pdf"]
yaxis = ["lin"]
stacksig = ["stack"]
# stacksig = ["stack", "nostack"]
fillsig = False
# scaleSig = 1.0
outdir = "/eos/user/a/almaloiz/thesis/fcc/plots/IDEA_newtagger/ZnunuHqq/"
xleg = 0.67
#Plots signal (resp. background) ordered by their yield
yieldOrder = False


variables = ['jet1_E', 'jet2_E', 'missing_e', 'higgs_hadronic_mass', 'mvis', 'higgs_hadronic_recoil_mass', 'mvis_zoom', 'higgs_hadronic_recoil_mass_zoom', 'jet1_nconst', 'jet2_nconst', 'higgs_hadronic_cos_theta', 'higgs_hadronic_cosSumThetaJJ', 'higgs_hadronic_cosDeltaPhiJJ', 'higgs_hadronic_cosDeltaPhiJJ_zoom', 'jets_d23', 'jets_d34', 'jets_d45', 'n_all_leptons', 'n_selected_leptons', 'leptons_p', 'pmiss']

# variables = ["m_recoil", "m_recoil_2"]

###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
# selections['ZH']   = ['Nosel','finalsel']
selections["ZH"] = [
   "nosel",  # for no selection at all
    # "sel_nolep",
    # "sel_jetE",
    # "sel_nconst",
    # "sel_pmiss",
    # "sel_cosThJJ",
    # "sel_cosSumThJJ",
    # "sel_dmerge",
    # "sel_mjj1",
    # "sel_cosDPhiJJ",
    # "trainNN",
    "sel_mvis_mmiss"
]

extralabel = {}
extralabel['nosel'] = 'No selection'
#extralabel['sel_cosDPhiJJ'] = 'Final selection'
extralabel['sel_mvis_mmiss'] = 'Final selection'
extralabel['selN_2b'] = '2b'
extralabel['selN_1b0c'] = '1b, 0c'
extralabel['selN_2c1b'] = '1b, 2c'
extralabel['selN_1b1c'] = '1b, 1c'
extralabel['selN_2c'] = '2c, <2b'
extralabel['selN_0b1c'] = '0b, 1c'
extralabel['selN_0b0c0g'] = '0b, 0c, 0g'
extralabel['selN_0b0c1g'] = '0b, 0c, 1g'
extralabel['selN_0b0c2g'] = '0b, 0c, 2g'


colors = {}
#colors['ZH'] = ROOT.kBlack
colors['ZHbb'] = ROOT.kRed-2
colors['ZHcc'] = ROOT.kPink+1
colors['ZHgg'] = ROOT.kOrange
colors['ZHss'] = ROOT.kRed+4
colors['ZHnonhad'] = ROOT.kBlack
colors['qqH'] = ROOT.kViolet
colors['WW'] = ROOT.kBlue+1
colors['ZZ'] = ROOT.kGreen+2
colors['nuenueZ'] = ROOT.kRed
colors['Zqq'] = ROOT.kCyan-3


plots = {}


plots['ZH'] = {
    'signal':
    {
        'ZHbb':['wzp6_ee_nunuH_Hbb_ecm240'],
        'ZHcc':['wzp6_ee_nunuH_Hcc_ecm240'],
        'ZHgg':['wzp6_ee_nunuH_Hgg_ecm240'],
        'ZHss':['wzp6_ee_nunuH_Hss_ecm240']
    },
    'backgrounds':
    {
        # 'WW':['p8_ee_WW_ecm240'],
        # 'ZZ':['p8_ee_ZZ_ecm240'],
        # 'Zqq': ['p8_ee_Zqq_ecm240'],
        # 'nuenueZ' : ['wzp6_ee_nuenueZ_ecm240'],
        'qqH':
        [
            'wzp6_ee_qqH_Hbb_ecm240',
            'wzp6_ee_qqH_Hcc_ecm240',
            'wzp6_ee_qqH_Hgg_ecm240',
            'wzp6_ee_qqH_Hss_ecm240',
            'wzp6_ee_qqH_HWW_ecm240',
            'wzp6_ee_qqH_HZZ_ecm240',
            'wzp6_ee_qqH_Htautau_ecm240',
            'wzp6_ee_ssH_Hbb_ecm240',
            'wzp6_ee_ssH_Hcc_ecm240',
            'wzp6_ee_ssH_Hgg_ecm240',
            'wzp6_ee_ssH_Hss_ecm240',
            'wzp6_ee_ssH_HWW_ecm240',
            'wzp6_ee_ssH_HZZ_ecm240',
            'wzp6_ee_ssH_Htautau_ecm240',
            'wzp6_ee_ccH_Hbb_ecm240',
            'wzp6_ee_ccH_Hcc_ecm240',
            'wzp6_ee_ccH_Hgg_ecm240',
            'wzp6_ee_ccH_Hss_ecm240',
            'wzp6_ee_ccH_HWW_ecm240',
            'wzp6_ee_ccH_HZZ_ecm240',
            'wzp6_ee_ccH_Htautau_ecm240',
            'wzp6_ee_bbH_Hbb_ecm240',
            'wzp6_ee_bbH_Hcc_ecm240',
            'wzp6_ee_bbH_Hgg_ecm240',
            'wzp6_ee_bbH_Hss_ecm240',
            'wzp6_ee_bbH_HWW_ecm240',
            'wzp6_ee_bbH_HZZ_ecm240',
            'wzp6_ee_bbH_Htautau_ecm240',
        ],
        'ZHnonhad':
        [
            'wzp6_ee_nunuH_HWW_ecm240',
            'wzp6_ee_nunuH_HZZ_ecm240',
            'wzp6_ee_nunuH_Htautau_ecm240'
        ],
    }
}

legend = {}
#legend['ZH'] = 'Total'
legend['ZHbb'] = '#nu#bar{#nu}H(b#bar{b})'
legend['ZHcc'] = '#nu#bar{#nu}H(c#bar{c})'
legend['ZHss'] = '#nu#bar{#nu}H(s#bar{s})'
legend['ZHgg'] = '#nu#bar{#nu}H(gg)'
legend['ZHnonhad'] = '#nu#bar{#nu}H(nonhad)'
legend['qqH'] = 'q#bar{q}H'
legend['ZZ'] = 'ZZ'
legend['WW'] = 'WW'
legend['Zqq'] = 'Z(q#bar{q})'
legend['nuenueZ'] = '#nu_{e}#bar{#nu}_{e}Z'
#legend['VV'] = 'VV boson'