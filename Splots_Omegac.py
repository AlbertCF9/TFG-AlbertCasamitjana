# . venv_Lb2ppimumu/bin/activate
import pandas as pd
import matplotlib.pyplot as plt


for i in ["LLL","DDL","DDD"]:

    pd_df = pd.read_csv(f"sweights_omegac_{i}.csv")

    
    plt.hist(pd_df["Omegac_M"] ,weights = pd_df["sweight_signal"],bins=50)
    plt.title("Splot Massa Omegac",fontsize=14)
    plt.xlabel("M Omegac (MeV/$c^2$)")
    plt.ylabel("Esdeveniments")
    plt.savefig(f"splot_omegac_{i}.pdf")
    plt.clf()