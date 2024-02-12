# Mandatory: List of processes
processList = {
    # Z(nunu)H
    #    'wzp6_ee_nunuH_Hbb_ecm240': {'chunks': 4},
    #    'wzp6_ee_nunuH_Hcc_ecm240': {'chunks': 4},
    #    'wzp6_ee_nunuH_Hss_ecm240': {'chunks': 4},
    #    'wzp6_ee_nunuH_Hgg_ecm240': {'chunks': 4},
    #    'wzp6_ee_nunuH_Htautau_ecm240': {'chunks': 4},
    #    'wzp6_ee_nunuH_HWW_ecm240': {'chunks': 4},
    #    'wzp6_ee_nunuH_HZZ_ecm240': {'chunks': 4},
    #     # Z(bb)H
    #      'wzp6_ee_bbH_Hbb_ecm240': {'chunks': 4},
    #      'wzp6_ee_bbH_Hcc_ecm240': {'chunks': 4},
    #      'wzp6_ee_bbH_Hss_ecm240': {'chunks': 4},
    #      'wzp6_ee_bbH_Hgg_ecm240': {'chunks': 4},
    #      'wzp6_ee_bbH_Htautau_ecm240': {'chunks': 4},
    #      'wzp6_ee_bbH_HWW_ecm240': {'chunks': 4},
    #      'wzp6_ee_bbH_HZZ_ecm240': {'chunks': 4},
    #     # # # Z(cc)H
    #      'wzp6_ee_ccH_Hbb_ecm240': {'chunks': 4},
    #      'wzp6_ee_ccH_Hcc_ecm240': {'chunks': 4},
    #      'wzp6_ee_ccH_Hss_ecm240': {'chunks': 4},
    #      'wzp6_ee_ccH_Hgg_ecm240': {'chunks': 4},
    #      'wzp6_ee_ccH_Htautau_ecm240': {'chunks': 4},
    #      'wzp6_ee_ccH_HWW_ecm240': {'chunks': 4},
    #      'wzp6_ee_ccH_HZZ_ecm240': {'chunks': 4},
    #     # # # Z(ss)H
    #      'wzp6_ee_ssH_Hbb_ecm240': {'chunks': 4},
    #      'wzp6_ee_ssH_Hcc_ecm240': {'chunks': 4},
    #      'wzp6_ee_ssH_Hss_ecm240': {'chunks': 4},
    #      'wzp6_ee_ssH_Hgg_ecm240': {'chunks': 4},
    #      'wzp6_ee_ssH_Htautau_ecm240': {'chunks': 4},
    #      'wzp6_ee_ssH_HWW_ecm240': {'chunks': 4},
    #      'wzp6_ee_ssH_HZZ_ecm240': {'chunks': 4},
    #     # # # Z(qq)H
    #      'wzp6_ee_qqH_Hbb_ecm240': {'chunks': 4},
    #      'wzp6_ee_qqH_Hcc_ecm240': {'chunks': 4},
    #      'wzp6_ee_qqH_Hss_ecm240': {'chunks': 4},
    #      'wzp6_ee_qqH_Hgg_ecm240': {'chunks': 4},
    #      'wzp6_ee_qqH_Htautau_ecm240': {'chunks': 4},
    #      'wzp6_ee_qqH_HWW_ecm240': {'chunks': 4},
    #      'wzp6_ee_qqH_HZZ_ecm240': {'chunks': 4},
        
        
        #bkg
        # 'p8_ee_WW_ecm240': {'chunks': 80},
        'p8_ee_ZZ_ecm240': {'chunks': 16},
        'p8_ee_Zqq_ecm240': {'chunks': 20},
        # 'wzp6_ee_nuenueZ_ecm240': {'chunks': 8},
        # 'wzp6_ee_mumu_ecm240',
        # 'wzp6_ee_ee_Mee_30_150_ecm240'
}


# Mandatory: Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics
prodTag = "FCCee/winter2023/IDEA/"

outputDirEos = "/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZnunuHqq/"
eosType = "eosuser"
# Optional: ncpus, default is 4
nCPUS = 8

# Optional running on HTCondor, default is False
runBatch = True

# Optional batch queue name when running on HTCondor, default is workday
batchQueue = "workday"

# Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
compGroup = "group_u_FCC.local_gen"

import ROOT

# ROOT.gErrorIgnoreLevel = ROOT.kFatal

# Optional
# nCPUS = 32

# runBatch = False
# batchQueue = "longlunch"
# compGroup = "group_u_FCC.local_gen"


import os, sys
import urllib.request


# ____________________________________________________________
def get_file_path(url, filename):
    if os.path.exists(filename):
        return os.path.abspath(filename)
    else:
        urllib.request.urlretrieve(url, os.path.basename(url))
        return os.path.basename(url)


# ____________________________________________________________


# ## tagger model
# model_name = "fccee_flavtagging_edm4hep_wc_v1"

# ## model files needed for unit testing in CI
# url_model_dir = "https://fccsw.web.cern.ch/fccsw/testsamples/jet_flavour_tagging/winter2023/wc_pt_13_01_2022/"
# url_preproc = "{}/{}.json".format(url_model_dir, model_name)
# url_model = "{}/{}.onnx".format(url_model_dir, model_name)

# ## model files locally stored on /eos
# model_dir = "/eos/experiment/fcc/ee/jet_flavour_tagging/winter2023/wc_pt_13_01_2022"
# local_preproc = "{}/{}.json".format(model_dir, model_name)
# local_model = "{}/{}.onnx".format(model_dir, model_name)

# ## get local file, else download from url
# weaver_preproc = get_file_path(url_preproc, local_preproc)
# weaver_model = get_file_path(url_model, local_model)

## latest particle transformer model, trainied on 9M jets in winter2023 samples
model_name = "fccee_flavtagging_edm4hep_wc"

## model files needed for unit testing in CI
url_model_dir = "https://fccsw.web.cern.ch/fccsw/testsamples/jet_flavour_tagging/winter2023/wc_pt_13_01_2022/"
url_preproc = "{}/{}.json".format(url_model_dir, model_name)
url_model = "{}/{}.onnx".format(url_model_dir, model_name)

## model files locally stored on /eos
# model_dir = "/eos/experiment/fcc/ee/jet_flavour_tagging/winter2023/wc_pt_13_01_2022/"
model_dir = (
    "/eos/experiment/fcc/ee/jet_flavour_tagging/winter2023/wc_pt_7classes_12_04_2023/"
)
local_preproc = "{}/{}.json".format(model_dir, model_name)
local_model = "{}/{}.onnx".format(model_dir, model_name)

## get local file, else download from url
weaver_preproc = get_file_path(url_preproc, local_preproc)
weaver_model = get_file_path(url_model, local_model)

# Fix to import following libraries from the ZxxHqq folders
# if os.getcwd().split("/")[-1] == "ZllHqq":
sys.path.append("/afs/cern.ch/user/a/almaloiz/eos/thesis/fcc/newAnalysis/FCCAnalyses/")

from addons.ONNXRuntime.python.jetFlavourHelper import JetFlavourHelper
from addons.FastJet.python.jetClusteringHelper import ExclusiveJetClusteringHelper

jetFlavourHelper = None
jetClusteringHelper = None

# jet_p_min = "15"
# jet_p_max = "100"
# lep_p_min = "25"
# lep_p_max = "80"

lep_p_min = "20"
lep_p_max = "99999"

# jet_p_min = '20'
# jet_p_max = '100'
# lep_p_min = '20'
# lep_p_max = '80'


# Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis:
    # __________________________________________________________
    # Mandatory: analysers funtion to define the analysers to process.
    # Note: make sure you return the last dataframe
    def analysers(df):
        global jetClusteringHelper
        global jetFlavourHelper

        # DO JET CLUSTERING AND FLAVOUR TAGGING
        njets = 2
        tag = ""
        collections = {
            "GenParticles": "Particle",
            "PFParticles": "ReconstructedParticles",
            "PFTracks": "EFlowTrack",
            "PFPhotons": "EFlowPhoton",
            "PFNeutralHadrons": "EFlowNeutralHadron",
            "TrackState": "EFlowTrack_1",
            "TrackerHits": "TrackerHits",
            "CalorimeterHits": "CalorimeterHits",
            "dNdx": "EFlowTrack_2",
            "PathLength": "EFlowTrack_L",
            "Bz": "magFieldBz",
        }

        # define jet clustering parameters
        jetClusteringHelper = ExclusiveJetClusteringHelper(
            collections["PFParticles"], njets, tag
        )

        ## run jet clustering
        df = jetClusteringHelper.define(df)

        ## define jet flavour tagging parameters
        jetFlavourHelper = JetFlavourHelper(
            collections,
            jetClusteringHelper.jets,
            jetClusteringHelper.constituents,
            tag,
        )

        ## define observables for tagger
        df = jetFlavourHelper.define(df)

        ## run tagger inference
        df = jetFlavourHelper.inference(weaver_preproc, weaver_model, df)

        ## calculate remaining variables
        df3 = (
            df
            # define some constants
            .Define("sqrts", "240.0")
            .Define("mZ", "91.2")
            # MC truth info
            .Alias("DaughtersIdx", "Particle#1.index")
            .Define(
                "MC_HiggsDecay",
                "FCCAnalyses::MCParticle::get_Higgs_decay()(Particle,DaughtersIdx)",
            )
            # get true flavour information of jets
            .Define(
                "jet_flavour", "JetTaggingUtils::get_flavour(jet, Particle, 2, 0.8)"
            )
            # jets
            # .Define('n_all_jets', 'JetClusteringUtils::get_n(jets)')
            .Define("jet1_E", "jet_e[0]")
            .Define("jet2_E", "jet_e[1]")
            # .Define('jet1_nconst', 'JetConstituentsUtils::count_consts(JetsConstituents)[0]')
            # .Define('jet2_nconst', 'JetConstituentsUtils::count_consts(JetsConstituents)[1]')
            .Define("jet1_nconst", "jet_nconst[0]")
            .Define("jet2_nconst", "jet_nconst[1]")
            .Define("jet1_isB", "recojet_isB[0]")
            .Define("jet1_isC", "recojet_isC[0]")
            .Define("jet1_isS", "recojet_isS[0]")
            # .Define("jet1_isQ", "recojet_isQ[0]")
            .Define("jet1_isU", "recojet_isU[0]")
            .Define("jet1_isD", "recojet_isD[0]")
            .Define("jet1_isTAU", "recojet_isTAU[0]")
            .Define("jet1_isG", "recojet_isG[0]")
            .Define("jet2_isB", "recojet_isB[1]")
            .Define("jet2_isC", "recojet_isC[1]")
            .Define("jet2_isS", "recojet_isS[1]")
            # .Define("jet2_isQ", "recojet_isQ[1]")
            .Define("jet2_isU", "recojet_isU[1]")
            .Define("jet2_isD", "recojet_isD[1]")
            .Define("jet2_isTAU", "recojet_isTAU[1]")
            .Define("jet2_isG", "recojet_isG[1]")
            # H->two jets
            .Define(
                "higgs_hadronic",
                "ReconstructedParticle::jetResonanceBuilder(125,1)(jet)",
            )
            .Define(
                "higgs_hadronic_m", "ReconstructedParticle::get_mass(higgs_hadronic)[0]"
            )
            .Define(
                "higgs_hadronic_E", "ReconstructedParticle::get_e(higgs_hadronic)[0]"
            )
            .Define(
                "higgs_hadronic_p", "ReconstructedParticle::get_p(higgs_hadronic)[0]"
            )
            .Define(
                "higgs_hadronic_cos_theta",
                "abs(cos(ReconstructedParticle::get_theta(higgs_hadronic)[0]))",
            )
            .Define(
                "higgs_hadronic_cos_dTheta_jj", "abs(cos(jet_theta[0] + jet_theta[1]))"
            )
            .Define("higgs_hadronic_cos_dPhi_jj", "abs(cos(jet_phi[0]-jet_phi[1]))")
            # calculate recoil of dijet system
            .Define(
                "higgs_hadronic_recoil",
                "ReconstructedParticle::recoilBuilder(sqrts)(higgs_hadronic)",
            )
            # calculate invariant mass of recoil system - should peak at m(Z) for Z(nunu)Z(had) and Z(nunu)H(had)
            .Define(
                "higgs_hadronic_recoil_m",
                "ReconstructedParticle::get_mass(higgs_hadronic_recoil)[0]",
            )
            #
            # ETmiss
            #
            # create branch with pmiss (just a renaming operation)
            # also create mmiss (which is just the recoil mass of the dijet system)
            .Define("pmiss", "MissingET.energy[0]")
            .Alias("mmiss", "higgs_hadronic_recoil_m")
            ##.Define('pmiss_E', 'sqrts-higgs_hadronic_E')
            ##.Define('pmiss_m', 'sqrt(pmiss_E*pmiss_E-pmiss_p*pmiss_p)')
            #
            # Calculate the corrected visible mass after rescaling the
            # visible energy and momentum by alpha such that m_miss = mZ
            #
            # (sqrtS, 0) = alpha (E_vis, p_vis) + (E_miss, p_miss)
            # => (sqrtS - alpha E_vis, - alpha p_vis) = (E_miss, p_miss)
            # => alpha^2 E_vis^2 - 2 alpha E_vis sqrtS + sqrtS^2 - alpha^2 p_vis^2 = mZ^2
            # => alpha^2 m_vis^2 - 2 alpha E_vis sqrtS + sqrtS^2-mZ^2 = 0
            # => alpha = [E_vis*sqrtS - sqrt(Delta)]/m_vis^2,
            #    Delta = E_vis^2 mZ^2 + p_vis^2(s-mZ^2)
            # => alpha*m_vis = E_vis/m_vis * sqrtS - sqrt(Delta/m_vis^2),
            #        where     Delta/m_vis^2 = (E_vis/m_vis)^2 mZ^2 + (p_vis/m_vis)^2 (sqrtS-mZ)(sqrtS+mZ)
            .Define("EvisOverMvis", "higgs_hadronic_E/higgs_hadronic_m")
            .Define("PvisOverMvis", "higgs_hadronic_p/higgs_hadronic_m")
            .Define(
                "DeltaOverMvisSq",
                "EvisOverMvis*EvisOverMvis*mZ*mZ + PvisOverMvis*PvisOverMvis*(sqrts+mZ)*(sqrts-mZ)",
            )
            .Define("mvis", "sqrts*EvisOverMvis - sqrt(DeltaOverMvisSq)")
            #
            # High-p leptons (to veto e.g. W(lnu)W(qq) bkg)
            # Ideally would use iso-leptons but we don't have them anymore
            #
            # define an alias for (isolated) muon index collection
            .Alias("Muon0", "Muon#0.index")
            # define the muon collection
            .Define(
                "muons", "ReconstructedParticle::get(Muon0, ReconstructedParticles)"
            )
            # define an alias for (isolated) electron index collection
            .Alias("Electron0", "Electron#0.index")
            # define the electron collection
            .Define(
                "electrons",
                "ReconstructedParticle::get(Electron0, ReconstructedParticles)",
            )
            # merge electrons and muons
            .Define("leptons", "ReconstructedParticle::merge(electrons, muons)")
            # select muons based on p
            .Define(
                "selected_muons",
                "ReconstructedParticle::sel_p("
                + lep_p_min
                + ","
                + lep_p_max
                + ")(muons)",
            )
            # select electrons based on p
            .Define(
                "selected_electrons",
                "ReconstructedParticle::sel_p("
                + lep_p_min
                + ","
                + lep_p_max
                + ")(electrons)",
            )
            # merge selected electrons and muons
            .Define(
                "selected_leptons",
                "ReconstructedParticle::merge(selected_electrons, selected_muons)",
            )
            .Define("n_all_leptons", "ReconstructedParticle::get_n(leptons)")
            .Define(
                "n_selected_leptons", "ReconstructedParticle::get_n(selected_leptons)"
            )
            .Define("leptons_p", "ReconstructedParticle::get_p(leptons)")
            .Define(
                "selected_leptons_p", "ReconstructedParticle::get_p(selected_leptons)"
            )
            .Define("event_d23", "JetClusteringUtils::get_exclusive_dmerge(_jet, 2)")
            .Define("event_d34", "JetClusteringUtils::get_exclusive_dmerge(_jet, 3)")
            .Define("event_d45", "JetClusteringUtils::get_exclusive_dmerge(_jet, 4)")
        )

        return df3

    # __________________________________________________________
    # SAVE PREDICTIONS & OBSERVABLES FOR ANALYSIS
    # Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
            "MC_HiggsDecay",
            "jet_flavour",
            "jet1_E",
            "jet1_nconst",
            "jet1_isB",
            "jet1_isC",
            "jet1_isS",
            # "jet1_isQ",
            "jet1_isU",
            "jet1_isD",
            "jet1_isTAU",
            "jet1_isG",
            "jet2_E",
            "jet2_nconst",
            "jet2_isB",
            "jet2_isC",
            "jet2_isS",
            # "jet2_isQ",
            "jet2_isU",
            "jet2_isD",
            "jet2_isTAU",
            "jet2_isG",
            "mvis",
            "higgs_hadronic_m",
            "higgs_hadronic_E",
            "higgs_hadronic_p",
            "higgs_hadronic_cos_theta",
            "higgs_hadronic_cos_dTheta_jj",
            "higgs_hadronic_cos_dPhi_jj",
            "higgs_hadronic_recoil_m",
            "pmiss",
            "n_all_leptons",
            "n_selected_leptons",
            "leptons_p",
            "selected_leptons_p",
            "event_d23",
            "event_d34",
            "event_d45",
        ]

        ##  outputs jet properties
        branchList += jetClusteringHelper.outputBranches()
        return branchList
