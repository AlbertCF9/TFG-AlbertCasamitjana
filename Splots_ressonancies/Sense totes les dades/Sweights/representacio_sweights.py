# . venv_Lb2ppimumu/bin/activate
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
      
for i in ["LLL","DDL","DDD"]:

    pd_df = pd.read_csv(f"sweights_omegac_{i}.csv")


    plt.hist(pd_df["sweight_signal"], bins=50)
    plt.title(f"Sweights_{i}",fontsize=14)
    plt.xlabel("Sweights")
    #plt.xlim(2000, 3000)
    plt.ylabel("Esdeveniments")
    plt.savefig(f"Plot_sweights_{i}.pdf")
    plt.clf()