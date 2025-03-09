import pandas
import pyroot


df = pyroot.RDataFrame("TupleOmegac2OmegaPiPiPi_DDL/DecayTree", "../00229334_00000001_1.hyperons.root")


pd_df = pandas.DataFrame(df.AsNumpy())#(columns=["Omegac_M"]))

import matplotlib.pyplot as plt
print(pd_df.keys())
plt.hist(pd_df["Omegac_M"], bins=100)
plt.savefig("test_plot.pdf")
print(pd_df)
