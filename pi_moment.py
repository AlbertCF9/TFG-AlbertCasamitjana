# . venv_Lb2ppimumu/bin/activate
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
      
for i in ["DDL","DDD"]:

    pd_df = pd.read_csv(f"sweights_omegac_{i}.csv")


    # Momentum
    for particle,color in zip(["pi_Omegac_1","pi_Omegac_2"],["blue","red"]):
        plt.hist(pd_df[f"{particle}_P"], bins=50,histtype='step', label=particle, color=color)


    plt.title(f"Momentum_pions_{i}",fontsize=14)
    plt.xlabel("Momentum (MeV/$c$)")
    plt.ylabel("Esdeveniments")
    plt.legend()
    plt.savefig(f"Momentum_pions_{i}.pdf")
    plt.clf()


    # Transversal momentum

    for particle,color in zip(["pi_Omegac_1","pi_Omegac_2"],["blue","red"]):
        pt = np.sqrt(pd_df[f"{particle}_PX"]**2 + pd_df[f"{particle}_PY"]**2)
        plt.hist(pt, bins=50,histtype='step', label=particle, color=color)

    plt.title(f"Transversal_momentum_pions_{i}",fontsize=14)
    plt.xlabel("Transversal momentum (MeV/$c$)")
    plt.ylabel("Esdeveniments")
    plt.legend()
    plt.savefig(f"Transversal_momentum_pions_{i}.pdf")
    plt.clf()


    #Pseudorapidity

    for particle,color in zip(["pi_Omegac_1","pi_Omegac_2"],["blue","red"]):
        eta = 0.5*np.log((pd_df[f"{particle}_P"]+pd_df[f"{particle}_PZ"])/(pd_df[f"{particle}_P"]-pd_df[f"{particle}_PZ"]))
        plt.hist(eta, bins=50,histtype='step', label=particle, color=color)
        
    plt.title(f"Pseudorapidity_pions_{i}",fontsize=14)
    plt.xlabel("Pseudorapidity")
    plt.ylabel("Esdeveniments")
    plt.legend()
    plt.savefig(f"Pseudorapidity_pions_{i}.pdf")
    plt.clf()
