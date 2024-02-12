#### to run : source analyse.sh

#Run dataframe analysis on locally generated files
analysis=analysis.py

detector=IDEA

# input files (from Pythia+Delphes)
path=/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/${detector}

# output path
# outputpath=/eos/user/g/gmarchio/fcc-new/ZllHqq/analysis/root/${detector}
# outputpath=./testAnalysis/
outputpath=/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZllHqq/

for process in \
    wzp6_ee_eeH_Hbb_ecm240 \
    # wzp6_ee_eeH_Hcc_ecm240 \
    # wzp6_ee_eeH_Hgg_ecm240 \
    # wzp6_ee_eeH_Hss_ecm240 \
    # wzp6_ee_eeH_Htautau_ecm240 \
    # wzp6_ee_eeH_HWW_ecm240 \
    # wzp6_ee_eeH_HZZ_ecm240 \
    # wzp6_ee_mumuH_Hbb_ecm240 \
    # wzp6_ee_mumuH_Hcc_ecm240 \
    # wzp6_ee_mumuH_Hgg_ecm240 \
    # wzp6_ee_mumuH_Hss_ecm240 \
    # wzp6_ee_mumuH_Htautau_ecm240 \
    # wzp6_ee_mumuH_HWW_ecm240 \
    # wzp6_ee_mumuH_HZZ_ecm240 \
    # p8_ee_ZZ_ecm240 \
    # p8_ee_WW_ecm240 \
    # p8_ee_Zqq_ecm240 \
    # wzp6_ee_mumu_ecm240 \
    # wzp6_ee_ee_Mee_30_150_ecm240 \
#
#    wzp6_ee_ZllHqq_ecm240 \
#    wzp6_ee_ZllHtt_ecm240 \
#    wzp6_ee_ZmmHnonhad_ecm240 \
#    wzp6_ee_ZeeHnonhad_ecm240 \
#    wzp6_ee_ZmmHcc_ecm240 \
#    wzp6_ee_ZeeHcc_ecm240 \
#    wzp6_ee_ZmmHgg_ecm240 \
#    wzp6_ee_ZeeHgg_ecm240 \
#    wzp6_ee_ZmmHbb_ecm240 \
#    wzp6_ee_ZeeHbb_ecm240 \
do
# everything but nonhad
    fccanalysis run $analysis --output ${outputpath}/${process}.root --files-list ${path}/${process}/events_*.root --nevents 100
# debug
#    fccanalysis run $analysis --output ${outputpath}/${process}.root --files-list ${path}/${process}/events_*.root  --nevents 1000
    echo ""
done