import ROOT as R

root_file= R.TFile("filtered_omegac.root")
dir = root_file.Get("TupleOmegac2OmegaPiPiPi_LLL_MagDown")
dir.ls() 
root_file.ls()