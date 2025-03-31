#lb-conda default
import ROOT
import pandas
import matplotlib.pyplot as plt
import numpy as np


for i in ["LLL","DDL","DDD"]:
    df = ROOT.RDataFrame(f"TupleOmegac2OmegaPiPiPi_{i}/DecayTree", "../00229334_00000001_1.hyperons.root")

    llista = [f"{particle}_P{component}" for particle in ["L0","K"] for component in ["E","X","Y","Z"]]

    pd_df = pandas.DataFrame(df.AsNumpy(columns=llista))
    E_total = 0
    px_total = 0
    py_total = 0
    pz_total = 0
    for particle in ["L0","K"]:
        E_total = E_total + pd_df[f"{particle}_PE"]
        px_total = px_total + pd_df[f"{particle}_PX"]
        py_total = py_total + pd_df[f"{particle}_PY"]
        pz_total = pz_total + pd_df[f"{particle}_PZ"]
        

    mass = np.sqrt(E_total**2-px_total**2-py_total**2-pz_total**2)

    plt.hist(mass, bins=100)
    plt.title(i,fontsize=14)
    plt.xlabel("Massa (MeV/c^2)")
    plt.ylabel("Frequencia")
    plt.savefig(f"massa_invariant_{i}.pdf")
    plt.clf()

