# . venv_Lb2ppimumu/bin/activate
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
      
def set_mpl_LHCb_style(climb_server=False):
    """
    function to set the LHCb style in matplotlib and recover the orginal color palette of matplotlib
    """
    import mplhep
    import matplotlib as mpl
    mplhep.style.use("LHCb2")

    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])

    mpl.rcParams["figure.autolayout"] = False
    
    if not climb_server: #FIXME: this should be removed in the future, when LaTeX is properly installed in CLIMB
        pgf_with_latex = {
                "text.usetex": True,
                "pgf.rcfonts": False,
                "pgf.preamble": r"\usepackage{color}"
                }

        mpl.rcParams.update(pgf_with_latex)

set_mpl_LHCb_style(climb_server=True)
#set_mpl_LHCb_style()
pd_df = pd.read_csv("sweights_omegac_DDD+DDL_final.csv")

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

plt.hist(mass_1,weights=pd_df["sweight_signal"], bins=40)

plt.xlabel(r"$m(\Omega^- \mathrm{\pi}_1^+ \mathrm{\pi}^-) - m(\Omega^-) + 1672.45 \ [\mathrm{MeV}/c^2]$")
plt.ylabel("Candidates / [MeV/$c^2$]")
plt.savefig(f"splot_omega_pi1_pi-_DDD+DDL_final.png")
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

plt.hist(mass_2,weights=pd_df["sweight_signal"], bins=40)

plt.xlabel(r"$m(\Omega^- \mathrm{\pi}_2^+ \mathrm{\pi}^-) - m(\Omega^-) + 1672.45 \ [\mathrm{MeV}/c^2]$")
plt.ylabel("Candidates / [MeV/$c^2$]")
plt.savefig(f"splot_omega_pi2_pi-_DDD+DDL_final.png")
plt.clf()




combined_masses = np.concatenate((mass_1, mass_2))
combined_weights = np.concatenate((pd_df["sweight_signal"], pd_df["sweight_signal"]))

#  Fer l’histograma

plt.hist(combined_masses, weights=combined_weights, bins=50)
plt.xlabel("M (Omega- pi, pi-) (MeV/$c^2$)")
plt.ylabel("Esdeveniments")
plt.savefig("splot_omega_combined_pions_DDD+DDL.png")
plt.clf()
