# . venv_Lb2ppimumu/bin/activate
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
      
for i in ["LLL","DDL","DDD"]:

    pd_df = pd.read_csv(f"sweights_omegac_{i}.csv")

    #llista = [f"{particle}_{component}" for particle in ["Omega","pi_Omegac_1","pi_mi_Omegac"] for component in ["PE","PX","PY","PZ"]]

    E_total_1 = 0
    px_total_1 = 0
    py_total_1 = 0
    pz_total_1 = 0
    for particle in ["Omega","pi_Omegac_1","pi_mi_Omegac"]:
        E_total_1 = E_total_1 + pd_df[f"{particle}_PE"]
        px_total_1 = px_total_1 + pd_df[f"{particle}_PX"]
        py_total_1 = py_total_1 + pd_df[f"{particle}_PY"]
        pz_total_1 = pz_total_1 + pd_df[f"{particle}_PZ"]

    mass_1 = np.sqrt(E_total_1**2-px_total_1**2-py_total_1**2-pz_total_1**2)

    plt.hist(mass_1,weights=pd_df["sweight_signal"], bins=30)
    
    plt.title(f"Splot M(O-,pi1,pi-)_{i}",fontsize=14)
    plt.xlabel("M (Omega- Pi1, Pi-) (MeV/$c^2$)")
    plt.ylabel("Esdeveniments")
    plt.savefig(f"splot_omega_pi1_pi-_{i}.pdf")
    plt.clf()

    # Segon grafic

    E_total_2 = 0
    px_total_2 = 0
    py_total_2 = 0
    pz_total_2 = 0
    for particle in ["Omega","pi_Omegac_2","pi_mi_Omegac"]:
        E_total_2 = E_total_2 + pd_df[f"{particle}_PE"]
        px_total_2 = px_total_2 + pd_df[f"{particle}_PX"]
        py_total_2 = py_total_2 + pd_df[f"{particle}_PY"]
        pz_total_2 = pz_total_2 + pd_df[f"{particle}_PZ"]

    mass_2 = np.sqrt(E_total_2**2-px_total_2**2-py_total_2**2-pz_total_2**2)

    plt.hist(mass_2,weights=pd_df["sweight_signal"], bins=30)
    
    plt.title(f"Splot M(O-,pi2,pi-)_{i}",fontsize=14)
    plt.xlabel("M (Omega- Pi2, Pi-) (MeV/$c^2$)")
    plt.ylabel("Esdeveniments")
    plt.savefig(f"splot_omega_pi2_pi-_{i}.pdf")
    plt.clf()

