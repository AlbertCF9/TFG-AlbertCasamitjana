# . venv_Lb2ppimumu/bin/activate
import pandas as pd
import matplotlib.pyplot as plt


for i in ["LLL","DDL","DDD"]:

    pd_df = pd.read_csv(f"sweights_{i}.csv")


    plt.hist(pd_df["Omega_M"],weights = pd_df["sweight_signal"], bins=100)
    plt.title("Splot Massa Omega-",fontsize=14)

    plt.xlabel("M Omega- (MeV/$c^2$)")
    plt.ylabel("Esdeveniments")
    plt.savefig(f"splot_omega-_{i}.pdf")
    plt.clf()