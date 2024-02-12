# do plots of histograms produced by finalSel

import ROOT
from ROOT import kRed, kPink, kOrange, kCyan, kBlue, kGreen, kViolet, kBlack
from ROOT import kDashed, gPad
from ROOT import TCanvas, THStack, TLegend, TFile, TLine, TH1D
import math

signalOnly = False
splitZHother = True

def PlotVars():

    # vars: varname, preselection, cutmin, cutmax, axis title, legend position, plot type
    vars = [
        # momentum of all leptons (Nosel)
        # ('all_leptons_p', 'Nosel', 25., 80., 'p(l_{rec}) [GeV]', 0.7, 'lin'),

         # type or reconstructed Z candidate (0=none, 1=Zee, 2=Zmm) (Nosel)
        # ('zed_flavour',   'Nosel', 0.5,    -9999., 'Z type', 0.7, 'lin'),

        #  # momentum of Z leptons (selN_Z)
        # ('zed_leptons_p', 'selN_Z', 9999., -9999., 'p(l_{Z}) [GeV]', 0.7, 'lin'),

        #  # zed candidate mass (selN_Z)
        # ('dilepton_mass_2', 'selN_Z', 81., 101.,   'm_{ll} [GeV]', 0.15, 'lin'),

        #  # zed candidate direction (selN_mZ)
        # ('cos_theta_Z', 'selN_mZ', 9999., 0.8,   '|cos#theta_{ll}|', 0.15, 'lin'),

        #  # leptonic recoil mass (selN_cos)
        # ('m_recoil_2', 'selN_cos', 120., 140.,   'm_{recoil} [GeV]', 0.15, 'lin'),

        #  # jets momenta (selN_H)
        # ('all_jets_p', 'selN_H', 15., 100.,   'p^{j} [GeV]', 0.7, 'lin'),
        # ('jets_p', 'selN_H', 9999., -9999.,   'p^{j} [GeV]', 0.7, 'lin'),

        #  # invariant mass of the jets (selN_H)
        # ('hadronic_mass_zoom', 'selN_H', 100., 140.,  'm_{jets} [GeV]', 0.15, 'lin'),

        #  # missing energy (selN_mhad)
        # ('missing_e',       'selN_H', 9999.,  30.,   'p_{miss} [GeV]', 0.7, 'lin'),

        #  # number of additional high-p electrons and muons (selN_miss)
        # ('N_extra_leptons', 'selN_miss', 0.5, -9999., 'N(l^{high p,extra})', 0.7, 'lin'),

        #  # dmerge (selN_miss)
        # ('jets_d23',       'selN_miss', 2.0,  -9999.,  'd_{23}', 0.7, 'log'),
        # ('jets_d34',       'selN_miss', 1.5,  -9999.,  'd_{34}', 0.7, 'log'),
        # ('jets_d45',       'selN_miss', 1.0,  -9999.,  'd_{45}', 0.7, 'log'),

        #  # tagger score
        # ('jet1_isB',       'trainNN', 9999., -9999.,  'isB(j1)', 0.7, 'log'),
        # ('jet2_isB',       'trainNN', 9999., -9999.,  'isB(j2)', 0.7, 'log'),
        # ('jet1_isC',       'trainNN', 9999., -9999.,  'isC(j1)', 0.7, 'log'),
        # ('jet2_isC',       'trainNN', 9999., -9999.,  'isC(j2)', 0.7, 'log'),
        # ('jet1_isG',       'trainNN', 9999., -9999.,  'isG(j1)', 0.7, 'log'),
        # ('jet2_isG',       'trainNN', 9999., -9999.,  'isG(j2)', 0.7, 'log'),
        # ('jet1_isS',       'trainNN', 9999., -9999.,  'isS(j1)', 0.7, 'log'),
        # ('jet2_isS',       'trainNN', 9999., -9999.,  'isS(j2)', 0.7, 'log'),
        # ('jet1_isU',       'trainNN', 9999., -9999.,  'isU(j1)', 0.7, 'log'),
        # ('jet2_isU',       'trainNN', 9999., -9999.,  'isU(j2)', 0.7, 'log'),
        # ('jet1_isD',       'trainNN', 9999., -9999.,  'isD(j1)', 0.7, 'log'),
        # ('jet2_isD',       'trainNN', 9999., -9999.,  'isD(j2)', 0.7, 'log'),
        # ('jet1_isTAU',       'trainNN', 9999., -9999.,  'isTAU(j1)', 0.7, 'log'),
        # ('jet2_isTAU',       'trainNN', 9999., -9999.,  'isTAU(j2)', 0.7, 'log'),

         # the other 4 vars used in the NN
        ('hadronic_mass',  'trainNN', 9999., -9999.,  'm_{jets} [GeV]', 0.7, 'lin'),
        ('missing_e',      'trainNN', 9999., -9999.,  'p_{miss} [GeV]', 0.7, 'lin'),

        ('jets_d23',       'trainNN', 9999., -9999.,  'd_{23}', 0.7, 'lin'),
        ('jets_d34',       'trainNN', 9999., -9999.,  'd_{34}', 0.7, 'lin'),
        
        # test alexis
        
        ("all_jets_p", "trainNN", 9999., -9999, 'p_{all_jets} [GeV]', 0.7, 'lin'),
        ("jets_p", "trainNN", 9999., -9999, 'p_{jets} [GeV]', 0.7, 'lin'),
        ("N_jets", "trainNN", 9999., -9999, 'N_{jets}', 0.7, 'lin'),
        ("m_jets", "trainNN", 9999., -9999, 'm_{jets} [GeV]', 0.7, 'lin'),
        ("p_Higgs", "trainNN", 9999., -9999, 'p_{Higgs} [GeV]', 0.7, 'lin'),
        ("p_Higgs_2", "trainNN", 9999., -9999, 'p_{Higgs}_2 [GeV]', 0.7, 'lin'),
        ("cos_theta_Z", "trainNN", 9999., -9999, 'cos(thetaZll)', 0.7, 'lin'),
        ("zed_leptonic_phi", "trainNN", 9999., -9999, 'Zll_phi', 0.7, 'lin'),
        ("dilepton_mass", "trainNN", 9999., -9999, 'm_{ll} [GeV]', 0.7, 'lin'),
        ("p_Higgs", "trainNN", 9999., -9999, 'p_{Higgs} [GeV]', 0.7, 'lin'),
        ("p_Higgs", "trainNN", 9999., -9999, 'p_{Higgs} [GeV]', 0.7, 'lin'),
    ]

    processes = [
        ['wzp6_ee_eeH_Hbb_ecm240',    'wzp6_ee_mumuH_Hbb_ecm240'],
        ['wzp6_ee_eeH_Hcc_ecm240',    'wzp6_ee_mumuH_Hcc_ecm240'],
        ['wzp6_ee_eeH_Hgg_ecm240',    'wzp6_ee_mumuH_Hgg_ecm240'],
        ['wzp6_ee_eeH_Hss_ecm240',    'wzp6_ee_mumuH_Hss_ecm240']]
    processLabels = [
        'llH(b#bar{b})',
        'llH(c#bar{c})',
        'llH(gg)',
        'llH(s#bar{s})']
    processColors = [
        kRed-2,
        kPink+1,
        kOrange,
        kCyan-6]

    if splitZHother:
        processes.extend([
            ['wzp6_ee_eeH_Htautau_ecm240','wzp6_ee_mumuH_Htautau_ecm240'],
            ['wzp6_ee_eeH_HWW_ecm240',    'wzp6_ee_mumuH_HWW_ecm240'],
            ['wzp6_ee_eeH_HZZ_ecm240',    'wzp6_ee_mumuH_HZZ_ecm240']
            ])
        processLabels.extend([
            'llH(#tau#tau)',
            'llH(WW)',
            'llH(ZZ)',
            ])
        processColors.extend([
            kViolet+1,
            kBlue,
            kGreen
            ])
    else:
        processes.extend([
            'wzp6_ee_eeH_Htautau_ecm240','wzp6_ee_mumuH_Htautau_ecm240',
            'wzp6_ee_eeH_HWW_ecm240',    'wzp6_ee_mumuH_HWW_ecm240',
            'wzp6_ee_eeH_HZZ_ecm240',    'wzp6_ee_mumuH_HZZ_ecm240'
        ])
        processLabels.extend(['llH(other)'])
        processColors.extend([kBlue])
        
    processes.extend([
        ['p8_ee_ZZ_ecm240'],
        # ['p8_ee_WW_ecm240'],
        ['p8_ee_Zqq_ecm240'],
        ['wzp6_ee_ee_Mee_30_150_ecm240', 'wzp6_ee_mumu_ecm240']
    ])
    processLabels.extend([
        'ZZ',
        # 'WW',
        'Z/#gamma*(q#bar{q})',
        'Z/#gamma*(ll)',
    ])
    processColors.extend([
        kGreen+2,
        # kRed,
        kViolet,
        kBlack
    ])

    baseDir = '/eos/user/a/almaloiz/thesis/fcc/root/IDEA_newtagger/ZllHqq/'
    plotpath = baseDir.replace('root','plots') + '/nostack'

    #Draw histos
    c = TCanvas('c', 'c', 800, 600)

    # loop over variables
    for iVar in range(len(vars)):
        var, sel, cutMin, cutMax, title, legPos, plotStyle = vars[iVar]
        print('Plotting variable ', var)
        
        # initialize stack and legend
        hs = THStack(var, '')
        leg = TLegend(legPos,0.6,legPos+0.18,0.88,'','brNDC')
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        
        # loop over the processes
        hist = {}
        for iProcess in range(len(processes)):

            procLabel = processLabels[iProcess]
            hist[iProcess] = TH1D()
            first = True
            for proc in processes[iProcess]:
                if (signalOnly and not 'wzp6_ee_eeH' in proc and not 'wzp6_ee_mumuH' in proc): continue

                # open file with histos
                fileName = '{:s}/finalsel/{:s}_{:s}_histo.root'.format(baseDir,proc,sel)
                print('Opening file ', fileName)
                f = TFile.Open(fileName, 'READ')

                # read histo
                print('Getting histogram ', var)
                h = f.Get(var)
                if first:
                    hist[iProcess] = h.Clone(procLabel)
                    first = False
                    hist[iProcess].SetLineColor(processColors[iProcess])
                    hist[iProcess].SetLineWidth(3)
                    hist[iProcess].SetDirectory(0)                  
                else:
                    hist[iProcess].Add(h)
                #h.SetDirectory(0)

                # set graphic attributes of histo
                #h.SetLineColor(processColors[iProcess])
                #h.SetLineWidth(3)

            # normalize histo to 1
            if hist[iProcess].Integral()!=0.0:
                hist[iProcess].Scale(1./hist[iProcess].Integral(), 'nosw2')

            # add histos to stack and legend
            # do not draw histograms with too few entries otherwise plot will have large spikes
            if hist[iProcess].GetEntries()>300.:
                hs.Add(hist[iProcess])
                leg.AddEntry(hist[iProcess],procLabel,'L')


        # draw the histo stack and legend
        c.Clear()
        hs.Draw('hist nostack')    
        hs.GetXaxis().SetTitle(title)
        leg.Draw()
        c.SetLogy(plotStyle=='log')
        gPad.Update()

        # draw the cuts
        print('Drawing cuts')
        yMax = c.GetUymax()
        yMin = c.GetUymin()
        if plotStyle=='log':
            yMax = math.pow(10,yMax)
            yMin = math.pow(10,yMin)
        if cutMin>-9999. :
            l1 = TLine(cutMin, yMin, cutMin, yMax)
            l1.SetLineStyle(kDashed)
            l1.SetLineColor(kBlack)
            l1.SetLineWidth(3)
            l1.Draw()
        if cutMax<9999. :
            l2 = TLine(cutMax, yMin, cutMax, yMax)
            l2.SetLineStyle(kDashed)
            l2.SetLineColor(kBlack)
            l2.SetLineWidth(3)
            l2.Draw()

        if signalOnly:
            c.Print('{:s}/{:s}_{:s}_signal.pdf'.format(plotpath,var,sel))
        else:
            c.Print('{:s}/{:s}_{:s}.pdf'.format(plotpath,var,sel))

if __name__ == "__main__":
    PlotVars()
