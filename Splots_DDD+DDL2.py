# . venv_Lb2ppimumu/bin/activate
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
      


pd_df = pd.read_csv("sweights_omegac_DDD+DDL.csv")

E_total_1 = 0
px_total_1 = 0
py_total_1 = 0
pz_total_1 = 0
for particle in ["Omega","pi_Omegac_1","pi_mi_Omegac"]:
    E_total_1 = E_total_1 + pd_df[f"{particle}_PE"]
    px_total_1 = px_total_1 + pd_df[f"{particle}_PX"]
    py_total_1 = py_total_1 + pd_df[f"{particle}_PY"]
    pz_total_1 = pz_total_1 + pd_df[f"{particle}_PZ"]

mass_1 = np.sqrt(E_total_1**2-px_total_1**2-py_total_1**2-pz_total_1**2) - pd_df["Omega_M"] + 1672.45  

plt.hist(mass_1,weights=pd_df["sweight_signal"], bins=30)

plt.title(f"Splot M(O-,pi1,pi-)_DDD+DDL",fontsize=14)
plt.xlabel("M (Omega- Pi1, Pi-) (MeV/$c^2$)")
plt.ylabel("Esdeveniments")
plt.savefig(f"splot_omega_pi1_pi-_DDD+DDL.png")
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

mass_2 = np.sqrt(E_total_2**2-px_total_2**2-py_total_2**2-pz_total_2**2) - pd_df["Omega_M"] + 1672.45  

plt.hist(mass_2,weights=pd_df["sweight_signal"], bins=30)

plt.title(f"Splot M(O-,pi2,pi-)_DDD+DDL",fontsize=14)
plt.xlabel("M (Omega- Pi2, Pi-) (MeV/$c^2$)")
plt.ylabel("Esdeveniments")
plt.savefig(f"splot_omega_pi2_pi-_DDD+DDL.png")
plt.clf()


combined_masses = np.concatenate((mass_1, mass_2))
combined_weights = np.concatenate((pd_df["sweight_signal"], pd_df["sweight_signal"]))

# Fer l’histograma
plt.hist(combined_masses, weights=combined_weights, bins=30)
plt.title("Splot M(O-, pi1/pi2, pi-) DDD+DDL", fontsize=14)
plt.xlabel("M (Omega- pi, pi-) (MeV/$c^2$)")
plt.ylabel("Esdeveniments")
plt.savefig("splot_omega_combined_pions_DDD+DDL.png")
plt.clf()