import ROOT
import pandas
import matplotlib.pyplot as plt

llista = ["Omegac_M","Omega_M"]

categories = ["LLL","DDL","DDD"]
dades_per_categoria = {cat: {} for cat in categories}
colors = {
    "LLL": "blue",
    "DDL": "green",
    "DDD": "red"
}

for i in categories:
    df = ROOT.RDataFrame(f"TupleOmegac2OmegaPiPiPi_{i}/DecayTree", "../00229334_00000001_1.hyperons.root")
    pd_df = pandas.DataFrame(df.AsNumpy(columns=llista))

    for j in llista:
        dades_per_categoria[i][j]= pd_df[j]


for j in llista:
    for i in categories:
        plt.hist(dades_per_categoria[i][j], bins=100, alpha=0.5, label=i,histtype='step', density=True, color = colors[i])

    
    plt.ylabel("Candidates (a.u.)")
    plt.legend()
    if j == "Omegac_M":
        plt.xlim(2600, 2780)
        plt.xlabel(r"$\it{m}(\Omega^{-} \pi^{+} \pi^{-} \pi^{+})\ [\mathrm{MeV}/\it{c}^2]$")

    else:
        plt.xlim(1640, 1705)
        plt.xlabel(r"$\it{m}(\Omega^{-})\ [\mathrm{MeV}/\it{c}^2]$")
        

    plt.savefig(f"{j}_normalitzats.png")
    plt.clf()
