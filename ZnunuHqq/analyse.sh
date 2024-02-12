#### to run : source analyse.sh

#Run dataframe analysis on locally generated files
analysis=analysis.py

detector=IDEA

# input files (from Pythia+Delphes)
path=/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/${detector}

# output path
# outputpath=/eos/user/g/gmarchio/fcc-new/ZllHqq/analysis/root/${detector}
outputpath=./testAnalysis/
# outputpath=/eos/user/a/almaloiz/thesis/fcc/root/IDEA/ZnunuHqq/

for process in \
    wzp6_ee_nunuH_Hbb_ecm240 \
    wzp6_ee_nunuH_Hgg_ecm240 \
    wzp6_ee_nunuH_HWW_ecm240 
    # wzp6_ee_ZnunuH_Hbb_ecm240 \
    # wzp6_ee_nunuH_Hcc_ecm240 \
    # wzp6_ee_nunuH_Hss_ecm240 \
    # wzp6_ee_nunuH_Htautau_ecm240 \
do
# everything but nonhad
    fccanalysis run $analysis --output ${outputpath}/${process}.root --files-list ${path}/${process}/events_*.root --nevents 10000
# debug
#    fccanalysis run $analysis --output ${outputpath}/${process}.root --files-list ${path}/${process}/events_*.root  --nevents 1000
    echo ""
done