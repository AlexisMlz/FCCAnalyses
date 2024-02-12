# Input directory where the files produced at the pre-selection level are
# inputDir  = "/eos/user/a/almaloiz/thesis/fcc/root/IDEA/ZllHqq/"
inputDir = "/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZnunuHqq/"
# inputDir = "./testAnalysis/"

# Input directory where the files produced at the pre-selection level are
outputDir = "/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZnunuHqq/finalsel/"

# processList = {"wzp6_ee_eeH_Hbb_ecm240": {}}

# Link to the dictonary that contains all the cross section informations etc...
procDict = "FCCee_procDict_winter2023_IDEA.json"

# Add MySample_p8_ee_ZH_ecm240 as it is not an offical process
# procDictAdd={"'wzp6_ee_eeH_Hbb_ecm240'":{"numberOfEvents": 10000000, "sumOfWeights": 10000000, "crossSection": 0.201868, "kfactor": 1.0, "matchingEfficiency": 1.0}}

# Number of CPUs to use
nCPUS = 32

# produces ROOT TTrees, default is False
doTree = True
do_NNvariables = True


process_list_sig ={
    # # nunuH
    # "wzp6_ee_nunuH_Hbb_ecm240": {},
    # "wzp6_ee_nunuH_Hcc_ecm240": {},
    # "wzp6_ee_nunuH_Hss_ecm240": {},
    # "wzp6_ee_nunuH_Hgg_ecm240": {},
    # "wzp6_ee_nunuH_Htautau_ecm240": {},
    # "wzp6_ee_nunuH_HWW_ecm240": {},
    # "wzp6_ee_nunuH_HZZ_ecm240": {},
    # # qqH (q=u,d)
    # "wzp6_ee_qqH_Hbb_ecm240": {},
    # "wzp6_ee_qqH_Hcc_ecm240": {},
    # "wzp6_ee_qqH_Hss_ecm240": {},
    # "wzp6_ee_qqH_Hgg_ecm240": {},
    # "wzp6_ee_qqH_Htautau_ecm240": {},
    # "wzp6_ee_qqH_HWW_ecm240": {},
    # "wzp6_ee_qqH_HZZ_ecm240": {},
    # # ssH
    # "wzp6_ee_ssH_Hbb_ecm240": {},
    # "wzp6_ee_ssH_Hcc_ecm240": {},
    # "wzp6_ee_ssH_Hss_ecm240": {},
    # "wzp6_ee_ssH_Hgg_ecm240": {},
    # "wzp6_ee_ssH_Htautau_ecm240": {},
    # "wzp6_ee_ssH_HWW_ecm240": {},
    # "wzp6_ee_ssH_HZZ_ecm240": {},
    # # ccH
    # "wzp6_ee_ccH_Hbb_ecm240": {},
    # "wzp6_ee_ccH_Hcc_ecm240": {},
    # "wzp6_ee_ccH_Hss_ecm240": {},
    # "wzp6_ee_ccH_Hgg_ecm240": {},
    # "wzp6_ee_ccH_Htautau_ecm240": {},
    # "wzp6_ee_ccH_HWW_ecm240": {},
    # "wzp6_ee_ccH_HZZ_ecm240": {},
    # # bbH
    # "wzp6_ee_bbH_Hbb_ecm240": {},
    # "wzp6_ee_bbH_Hcc_ecm240": {},
    # "wzp6_ee_bbH_Hss_ecm240": {},
    # "wzp6_ee_bbH_Hgg_ecm240": {},
    # "wzp6_ee_bbH_Htautau_ecm240": {},
    # "wzp6_ee_bbH_HWW_ecm240": {},
    # "wzp6_ee_bbH_HZZ_ecm240": {},
}
process_list_bkg = {
    # bkg
    # "wzp6_ee_nuenueZ_ecm240": {},
    # "p8_ee_Zqq_ecm240": {},
    "p8_ee_ZZ_ecm240": {},
    "p8_ee_WW_ecm240": {},
}
processList = process_list_sig | process_list_bkg
# processList=[
#     'wzp6_ee_eeH_Hbb_ecm240']

sel_nolep = "n_selected_leptons<1"
sel_jetE = sel_nolep + " && jet1_E>45 && jet1_E<105 && jet2_E>20 && jet2_E<70"
# sel_nconst = sel_jetE + " && jet1_nconst>10 && jet2_nconst>6"
sel_nconst = sel_jetE 
# sel_pmiss = sel_nconst + ' && pmiss>20 && pmiss<70'
sel_pmiss = sel_nconst
sel_cosThJJ = sel_pmiss + " && higgs_hadronic_cos_theta<0.92"
sel_cosSumThJJ = sel_cosThJJ + " && higgs_hadronic_cos_dTheta_jj>0.5"
# sel_dmerge = sel_cosSumThJJ + ' && event_d45<100 && event_d34<250 && event_d23<500'
sel_dmerge = sel_cosSumThJJ
# sel_mjj1 = sel_dmerge + ' && higgs_hadronic_m>100 && higgs_hadronic_m<135'
sel_mjj1 = sel_dmerge
sel_cosDPhiJJ = sel_mjj1 + " && higgs_hadronic_cos_dPhi_jj<0.999"
sel_mvis_mmiss = (
    sel_cosDPhiJJ
    + " && mvis > 70 && mvis < 150 && higgs_hadronic_recoil_m>50 && higgs_hadronic_recoil_m<140"
)

###Dictionary of the list of cuts. The key is the name of the selection that will be added to the output file.
cutList = {
    "nosel": "1==1",  # for no selection at all
    "sel_nolep": sel_nolep,
    "sel_jetE": sel_jetE,
    "sel_nconst": sel_nconst,
    "sel_pmiss": sel_pmiss,
    "sel_cosThJJ": sel_cosThJJ,
    "sel_cosSumThJJ": sel_cosSumThJJ,
    "sel_dmerge": sel_dmerge,
    "sel_mjj1": sel_mjj1,
    "sel_cosDPhiJJ": sel_cosDPhiJJ,
    "trainNN": sel_cosDPhiJJ,
    "sel_mvis_mmiss": sel_mvis_mmiss,
}
# final_selec = sel_cosDPhiJJ
final_selec = sel_mvis_mmiss


histoList = {}

if do_NNvariables == True:
    histoList = {
        #    'n_btags'   : {'name':'n_selected_btagged_jets','title':'N_{b-tags}','bin':3,'xmin':-0.5,'xmax':2.5},
        #    'n_ctags'   : {'name':'n_selected_ctagged_jets','title':'N_{c-tags}','bin':3,'xmin':-0.5,'xmax':2.5},
        #    'n_gtags'   : {'name':'n_selected_gtagged_jets','title':'N_{g-tags}','bin':3,'xmin':-0.5,'xmax':2.5},
        "higgs_hadronic_mass": {
            "name": "higgs_hadronic_m",
            "title": "m_{jj} [GeV]",
            "bin": 80,
            "xmin": 100,
            "xmax": 135,
        },
        "missing_e": {
            "name": "pmiss",
            "title": "p_{miss} [GeV]",
            "bin": 80,
            "xmin": 20,
            "xmax": 100,
        },
        "mvis": {
            "name": "mvis",
            "title": "m_{vis} [GeV]",
            "bin": 80,
            "xmin": 70,
            "xmax": 150,
        },
        "mmiss": {
            "name": "higgs_hadronic_recoil_m",
            "title": "m_{miss} [GeV]",
            "bin": 150,
            "xmin": 20,
            "xmax": 170,
        },
        "HiggsDecay": {
            "name": "MC_HiggsDecay",
            "title": "Higgs decay",
            "bin": 70,
            "xmin": 0,
            "xmax": 70,
        },
        "jet1_isB": {
            "name": "jet1_isB",
            "title": "isB(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isC": {
            "name": "jet1_isC",
            "title": "isC(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isG": {
            "name": "jet1_isG",
            "title": "isG(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isS": {
            "name": "jet1_isS",
            "title": "isS(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isU": {
            "name": "jet1_isU",
            "title": "isU(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isD": {
            "name": "jet1_isD",
            "title": "isD(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isB": {
            "name": "jet2_isB",
            "title": "isB(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isC": {
            "name": "jet2_isC",
            "title": "isC(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isG": {
            "name": "jet2_isG",
            "title": "isG(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isS": {
            "name": "jet2_isS",
            "title": "isS(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isU": {
            "name": "jet2_isU",
            "title": "isU(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isD": {
            "name": "jet2_isD",
            "title": "isD(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        #    'jets_d23' : {'name':'event_d23','title':'d_{23}','bin':50,'xmin':0,'xmax':500},
        #    'jets_d34' : {'name':'event_d34','title':'d_{34}','bin':50,'xmin':0,'xmax':250},
        #    'jets_d45' : {'name':'event_d45','title':'d_{45}','bin':50,'xmin':0,'xmax':100},
        "jets_d23": {
            "name": "event_d23",
            "title": "d_{23}",
            "bin": 50,
            "xmin": 0,
            "xmax": 2500,
        },
        "jets_d34": {
            "name": "event_d34",
            "title": "d_{34}",
            "bin": 50,
            "xmin": 0,
            "xmax": 1000,
        },
        "jets_d45": {
            "name": "event_d45",
            "title": "d_{45}",
            "bin": 50,
            "xmin": 0,
            "xmax": 500,
        },
    }

else:
    histoList = {
        "jet1_E": {
            "name": "jet1_E",
            "title": "Jet1 E [GeV]",
            "bin": 70,
            "xmin": 0,
            "xmax": 140,
        },
        "jet2_E": {
            "name": "jet2_E",
            "title": "Jet2 E [GeV]",
            "bin": 70,
            "xmin": 0,
            "xmax": 140,
        },
        #    'N_btag_jets':{'name':'n_selected_btagged_jets','title':'Number of b-tagged jets','bin':3,'xmin':0,'xmax':3},
        #    'N_ctag_jets':{'name':'n_selected_ctagged_jets','title':'Number of c-tagged jets','bin':3,'xmin':0,'xmax':3},
        #    'N_gtag_jets':{'name':'n_selected_gtagged_jets','title':'Number of g-tagged jets','bin':3,'xmin':0,'xmax':3},
        "missing_e": {
            "name": "pmiss",
            "title": "p_{miss} [GeV]",
            "bin": 60,
            "xmin": 0,
            "xmax": 120,
        },
        "higgs_hadronic_mass": {
            "name": "higgs_hadronic_m",
            "title": "Dijet invariant mass [GeV]",
            "bin": 80,
            "xmin": 70,
            "xmax": 150,
        },
        #
        "mvis": {
            "name": "mvis",
            "title": "Visible mass [GeV]",
            "bin": 120,
            "xmin": 60,
            "xmax": 180,
        },
        "higgs_hadronic_recoil_mass": {
            "name": "higgs_hadronic_recoil_m",
            "title": "m_{miss} [GeV]",
            "bin": 150,
            "xmin": 20,
            "xmax": 170,
        },
        #
        "mvis_zoom": {
            "name": "mvis",
            "title": "Visible mass [GeV]",
            "bin": 80,
            "xmin": 70,
            "xmax": 150,
        },
        "higgs_hadronic_recoil_mass_zoom": {
            "name": "higgs_hadronic_recoil_m",
            "title": "m_{miss} [GeV]",
            "bin": 90,
            "xmin": 50,
            "xmax": 140,
        },
        #
        "jet1_nconst": {
            "name": "jet1_nconst",
            "title": "Nparts in Jets 1",
            "bin": 60,
            "xmin": 0,
            "xmax": 60,
        },
        "jet2_nconst": {
            "name": "jet2_nconst",
            "title": "Nparts in Jets 2",
            "bin": 60,
            "xmin": 0,
            "xmax": 60,
        },
        "higgs_hadronic_cos_theta": {
            "name": "higgs_hadronic_cos_theta",
            "title": "|cos({theta}_{jj})|",
            "bin": 50,
            "xmin": 0,
            "xmax": 1,
        },
        "higgs_hadronic_cosSumThetaJJ": {
            "name": "higgs_hadronic_cos_dTheta_jj",
            "title": "|cos(#theta_{j1}+#theta_{j2})|",
            "bin": 50,
            "xmin": 0,
            "xmax": 1,
        },
        "higgs_hadronic_cosDeltaPhiJJ": {
            "name": "higgs_hadronic_cos_dPhi_jj",
            "title": "cos(#phi_{j1}-#phi_{j2})",
            "bin": 50,
            "xmin": 0,
            "xmax": 1,
        },
        "higgs_hadronic_cosDeltaPhiJJ_zoom": {
            "name": "higgs_hadronic_cos_dPhi_jj",
            "title": "cos(#phi_{j1}-#phi_{j2})",
            "bin": 100,
            "xmin": 0.95,
            "xmax": 1,
        },
        "jets_d23": {
            "name": "event_d23",
            "title": "d_{23}",
            "bin": 50,
            "xmin": 0,
            "xmax": 2500,
        },
        "jets_d34": {
            "name": "event_d34",
            "title": "d_{34} jet distance",
            "bin": 50,
            "xmin": 0,
            "xmax": 1000,
        },
        "jets_d45": {
            "name": "event_d45",
            "title": "d_{45}",
            "bin": 50,
            "xmin": 0,
            "xmax": 500,
        },
        "n_all_leptons": {
            "name": "n_all_leptons",
            "title": "N(leptons)",
            "bin": 3,
            "xmin": 0,
            "xmax": 3,
        },
        "n_selected_leptons": {
            "name": "n_selected_leptons",
            "title": "N(high-p leptons)",
            "bin": 3,
            "xmin": 0,
            "xmax": 3,
        },
        "leptons_p": {
            "name": "leptons_p",
            "title": "p(leptons)",
            "bin": 100,
            "xmin": 0,
            "xmax": 100,
        },
        "pmiss": {
            "name": "pmiss",
            "title": "p_{miss} [GeV]",
            "bin": 50,
            "xmin": 20,
            "xmax": 70,
        },
        "jet1_isB": {
            "name": "jet1_isB",
            "title": "isB(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isC": {
            "name": "jet1_isC",
            "title": "isC(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isG": {
            "name": "jet1_isG",
            "title": "isG(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isS": {
            "name": "jet1_isS",
            "title": "isS(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isU": {
            "name": "jet1_isU",
            "title": "isU(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet1_isD": {
            "name": "jet1_isD",
            "title": "isD(j1)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isB": {
            "name": "jet2_isB",
            "title": "isB(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isC": {
            "name": "jet2_isC",
            "title": "isC(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isG": {
            "name": "jet2_isG",
            "title": "isG(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isS": {
            "name": "jet2_isS",
            "title": "isS(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isU": {
            "name": "jet2_isU",
            "title": "isU(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        },
        "jet2_isD": {
            "name": "jet2_isD",
            "title": "isD(j2)",
            "bin": 100,
            "xmin": 0.0,
            "xmax": 1.0,
        }
    }
