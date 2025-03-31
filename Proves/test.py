#lb-conda default
import ROOT
import pandas
import matplotlib.pyplot as plt


for i in ["LLL","DDL","DDD"]:
    df = ROOT.RDataFrame(f"TupleOmegac2OmegaPiPiPi_{i}/DecayTree", "../00229334_00000001_1.hyperons.root")

    llista = ["Omegac_M","Omegac_OWNPV_CHI2","Omegac_PHI","Omegac_PT","Omegac_IP_OWNPV","Omega_M"]

    #pd_df = pandas.DataFrame(df.AsNumpy())

    pd_df = pandas.DataFrame(df.AsNumpy(columns=llista))

    for j in llista:
        plt.hist(pd_df[j], bins=100)
        plt.title(j+i,fontsize=14)
        plt.xlabel("x")
        plt.ylabel("Frequencia")
        #plt.xlim(-25,25) #Rang eix x
        plt.savefig(f"{j}{i}.pdf")
        plt.clf()
