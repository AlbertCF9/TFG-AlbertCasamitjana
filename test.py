import ROOT
import pandas
import matplotlib.pyplot as plt


df = ROOT.RDataFrame("TupleOmegac2OmegaPiPiPi_DDL/DecayTree", "../00229334_00000001_1.hyperons.root")
print("1")
pd_df = pandas.DataFrame(df.AsNumpy())#(columns=["Omegac_M"]))
print("2")
print(pd_df.keys())
print("3")
plt.hist(pd_df["Omegac_M"], bins=100)
plt.savefig("test_plot2.pdf")
print(pd_df)