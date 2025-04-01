import ROOT as R 

R.RooMsgService.instance().setGlobalKillBelow(R.RooFit.ERROR)
R.RooMsgService.instance().setSilentMode(R.kTRUE)

R.gROOT.ProcessLine(".x lhcbStyle.C")

for i in ["LLL","DDL","DDD"]:

    tree = f"TupleOmegac2OmegaPiPiPi_{i}/DecayTree"
    root_file = "../00229334_00000001_1.hyperons.root"

    df = R.RDataFrame(tree, root_file)

    filtered_df = df.Filter("abs(Omega_M-1672) < 15") \
                    .Filter("abs(L0_M-1115.7) < 10") \
                    .Filter("Omegac_PT > 1500") \
                    .Filter("pi_Omegac_1_PT > 350")\
                    .Filter("pi_Omegac_2_PT > 350") \
                    .Filter("Omegac_FDCHI2_OWNPV > 15")\
                    .Filter("Omega_FDCHI2_OWNPV > 30") \
                    .Filter("pi_Omegac_1_IPCHI2_OWNPV > 1.9 && pi_Omegac_1_IPCHI2_OWNPV < 3")\
                    .Filter("pi_Omegac_2_IPCHI2_OWNPV > 1.9 && pi_Omegac_2_IPCHI2_OWNPV < 3")\
                    .Filter("Omegac_ENDVERTEX_CHI2 < 9") \

#.Filter("Omega_FDCHI2_ORIVX > 30") No se quin dels dos utilitzar, orivx, basat en el punt de desintegració inicial
#ownpv trajectoria basat en el punt de producció de la particula

    print(f"Total d'entrades abans del filtre: {df.Count().GetValue()}")
    print(f"Total d'entrades després del filtre: {filtered_df.Count().GetValue()}")

    filtered_df.Snapshot(tree,f"filtered_omegac_{i}.root")