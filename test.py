import ROOT
import pandas
import matplotlib.pyplot as plt

df = ROOT.RDataFrame("TupleOmegac2OmegaPiPiPi_DDL/DecayTree", "../00229334_00000001_1.hyperons.root")

#pd_df = pandas.DataFrame(df.AsNumpy())

#Vertex fit quality omegac
#pd_df = pandas.DataFrame(df.AsNumpy(columns=["Omegac_OWNPV_CHI2"]))
#Direction angle omegac
#pd_df = pandas.DataFrame(df.AsNumpy(columns=["Omegac_PHI"]))
#Transversal moment omegac
#pd_df = pandas.DataFrame(df.AsNumpy(columns=["Omegac_PT"]))
#Omegac mass
#pd_df = pandas.DataFrame(df.AsNumpy(columns=["Omegac_M"]))
#Omegac impact parameter
pd_df = pandas.DataFrame(df.AsNumpy(columns=["Omegac_IPCHI2_OWNPV"]))
#No entenc el grafic

#Omega  decay Length
#pd_df = pandas.DataFrame(df.AsNumpy(columns=["Omegac_DTF_Omegaminus_decayLength"]))
# Aquest no ha sortit


#titols = pd_df.iloc[0]
#titols.to_csv('titols.txt',sep='\t')
#print(pd_df.keys())

plt.hist(pd_df["Omegac_IPCHI2_OWNPV"], bins=100)
plt.title("Omegac impact parameter",fontsize=14)
plt.xlabel("u.a.")
plt.ylabel("Frequencia")
#plt.xlim(-25,25) #Rang eix x
plt.savefig("Impact_parameter_omegac.pdf")


#print(pd_df)