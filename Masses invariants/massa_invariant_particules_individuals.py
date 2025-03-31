#lb-conda default
import ROOT
import pandas
import matplotlib.pyplot as plt
import numpy as np


for i in ["LLL","DDL","DDD"]:
    df = ROOT.RDataFrame(f"TupleOmegac2OmegaPiPiPi_{i}/DecayTree", "../00229334_00000001_1.hyperons.root")

    llista = [f"{particle}_P{component}" for particle in ["Omega","L0","K"] for component in ["E","X","Y","Z"]]

    pd_df = pandas.DataFrame(df.AsNumpy(columns=llista))
    
    for particle in ["Omega","L0","K"]:
        mass = np.sqrt(pd_df[f"{particle}_PE"]**2-pd_df[f"{particle}_PX"]**2-pd_df[f"{particle}_PY"]**2-pd_df[f"{particle}_PZ"]**2)
        plt.hist(mass, bins=100)
        plt.title(particle+i,fontsize=14)
        plt.xlabel("Massa (MeV/c^2)")
        plt.ylabel("Frequencia")
        plt.savefig(f"massa_invariant_{particle}_{i}.pdf")
        plt.clf()
