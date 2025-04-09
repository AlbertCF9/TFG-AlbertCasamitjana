# . venv_Lb2ppimumu/bin/activate

import ROOT as R 
import glob

R.RooMsgService.instance().setGlobalKillBelow(R.RooFit.ERROR)
R.RooMsgService.instance().setSilentMode(R.kTRUE)

R.gROOT.ProcessLine(".x lhcbStyle.C")


for i in ["LLL","DDL","DDD"]:

    tree = f"TupleOmegac2OmegaPiPiPi_{i}/DecayTree"
    root_files_MagUp = glob.glob("/home/lcalefice/hyperon_spectroscopy/tuples/Run_2_TurboLines/Omegac2OmegaPiPiPi/data/2018/MagUp/*.root")
    root_files_MagDown = glob.glob("/home/lcalefice/hyperon_spectroscopy/tuples/Run_2_TurboLines/Omegac2OmegaPiPiPi/data/2018/MagUp/*.root")

    root_files = root_files_MagDown + root_files_MagUp

    df = R.RDataFrame(tree, root_files)

    filtered_df = df.Filter("Omegac_PT > 1500") \
                    .Filter("pi_Omegac_1_PT > 350")\
                    .Filter("pi_Omegac_2_PT > 350") \
                    .Filter("pi_mi_Omegac_PT > 350") \
                    .Filter("Omegac_ENDVERTEX_CHI2 < 9") \
                    .Filter("sqrt(pow(Omegac_ENDVERTEX_X - Omegac_OWNPV_X, 2) + pow(Omegac_ENDVERTEX_Y - Omegac_OWNPV_Y, 2)) > 0.1")\
                    .Filter("-sqrt(pow(Omegac_ENDVERTEX_X - Omegac_OWNPV_X, 2) + pow(Omegac_ENDVERTEX_Y - Omegac_OWNPV_Y, 2)) + sqrt(pow(Omega_ENDVERTEX_X - Omega_OWNPV_X, 2) + pow(Omega_ENDVERTEX_Y - Omega_OWNPV_Y, 2)) > 0.1")\
                    .Filter("-sqrt(pow(Omega_ENDVERTEX_X - Omega_OWNPV_X, 2) + pow(Omega_ENDVERTEX_Y - Omega_OWNPV_Y, 2)) + sqrt(pow(L0_ENDVERTEX_X - L0_OWNPV_X, 2) + pow(L0_ENDVERTEX_Y - L0_OWNPV_Y, 2)) > 0.05")\
                    .Filter("Omegac_DIRA_OWNPV > 0.9999")\
                    .Filter("Omegac_FDCHI2_OWNPV > 15")\
                    .Filter("Omega_FDCHI2_OWNPV > 30") \
                    .Filter("pi_Omegac_1_ProbNNpi*(1-pi_Omegac_1_ProbNNk) > 0.4")\
                    .Filter("pi_Omegac_2_ProbNNpi*(1-pi_Omegac_2_ProbNNk) > 0.4")\
                    .Filter("pi_mi_Omegac_ProbNNpi*(1-pi_mi_Omegac_ProbNNk) > 0.4")\
                    .Filter("pi_Omegac_1_TRACK_GhostProb < 0.3")\
                    .Filter("pi_Omegac_2_TRACK_GhostProb < 0.3")\
                    .Filter("pi_mi_Omegac_TRACK_GhostProb < 0.3")\
                    .Filter("Omega_ENDVERTEX_Z - Omegac_ENDVERTEX_Z > 0")\
                    .Filter("L0_ENDVERTEX_Z - Omega_ENDVERTEX_Z > 0")\
                    .Filter("abs(L0_M-1115.7) < 10") \
                    .Filter("abs(Omega_M-1672) < 15") \    
                    .Filter("TMath::Max(pi_Omegac_1_PT,TMath::Max(pi_Omegac_2_PT,pi_mi_Omegac_PT)) > 400")\
                    .Filter("TMath::Max(pi_Omegac_1_IPCHI2_OWNPV,TMath::Max(pi_Omegac_2_IPCHI2_OWNPV,pi_mi_Omegac_IPCHI2_OWNPV)) > 3")\
                    .Filter("TMath::Min(pi_Omegac_1_IPCHI2_OWNPV,TMath::Min(pi_Omegac_2_IPCHI2_OWNPV,pi_mi_Omegac_IPCHI2_OWNPV)) > 1.9")\
                
                
    print(f"Total d'entrades abans del filtre: {df.Count().GetValue()}")
    print(f"Total d'entrades després del filtre: {filtered_df.Count().GetValue()}")
    filtered_df.Snapshot(f"TupleOmegac2OmegaPiPiPi_{i}/DecayTree",f"filtered_omegac_{i}.root",["Omegac_M"])