# lb-conda-dev virtual-env default/2024-06-23 venv_Lb2ppimumu
# . venv_Lb2ppimumu/bin/activate
import ROOT as R

R.RooMsgService.instance().setGlobalKillBelow(R.RooFit.ERROR)
R.RooMsgService.instance().setSilentMode(R.kTRUE)

R.gROOT.ProcessLine(".x lhcbStyle.C")

tree = "TupleOmegac2OmegaPiPiPi_DDL/DecayTree"
root_file = "../00229334_00000001_1.hyperons.root"

df = R.RDataFrame(tree, root_file)

print(df.Count().GetValue())

df.Snapshot(tree, "test.root", ["Omega_M"])

#Define the range
x_lower = 1640
x_upper = 1710
x_range = R.RooRealVar("Omega_M", "Omega_M", x_lower, x_upper)

#Read the data file
data = R.TChain("ch_data")

data.Add(f"test.root/{tree}")

print(data.GetEntries())
RDS_data = R.RooDataSet("a_data", "a_data",data, R.RooArgSet(x_range))
RDS_data = RDS_data.reduce((R.RooFit.CutRange("Omega_M")))
entries_data = RDS_data.sumEntries()

# Define the signal model pdf
mean = R.RooRealVar("#mu", "mean", 1670, 1650, 1690)
sigma = R.RooRealVar("#sigma", "sigma", 1, 0.1, 30)
Gaussian = R.RooGaussian('Gaussian', 'Gaussian', x_range, mean, sigma)

# Define the background model pdf
c = R.RooRealVar("c", "c", 0, -1, 1)  
Exponential = R.RooExponential("Exponential", "Exponential", x_range, c)

# Build composite pdf
sig_yield = R.RooRealVar("N_{sig}", "Signal yield", entries_data*0.2, 0, 1.2*entries_data)
bkg_yield = R.RooRealVar("N_{bkg}", "Background yield", entries_data*0.8, 0, 1.2*entries_data)
model = R.RooAddPdf("model", "model", R.RooArgList(Gaussian, Exponential), R.RooArgList(sig_yield, bkg_yield))

#make the fit
results = model.fitTo(RDS_data, R.RooFit.Save(True))
xframe = x_range.frame(R.RooFit.Title(f"Fit Result"))

RDS_data.plotOn(xframe, R.RooFit.Name("Data"))  # Plot the data points
model.plotOn(xframe, R.RooFit.LineColor(R.kBlue), R.RooFit.Name("PDF"))  # Plot the fit model
model.plotOn(xframe, R.RooFit.Components("Gaussian"), R.RooFit.LineColor(R.kGreen), R.RooFit.LineStyle(R.kDashed), R.RooFit.Name("Signal"))
# Plot the Chebychev with proper scaling
model.plotOn(xframe, R.RooFit.Components("Exponential"), R.RooFit.LineColor(R.kRed), R.RooFit.LineStyle(R.kDashed), R.RooFit.Name("Background"))
model.paramOn(xframe, R.RooFit.Layout(0.65, 0.75, 0.6))    

xframe.GetXaxis().SetTitle("#it{m}(" + '#Omega^{-}'+"[MeV/#it{c}^{2}]")

bin_width = (x_upper-x_lower)/100
xframe.GetYaxis().SetTitle(f"Candidates/({bin_width}MeV/c^{2})")

c = R.TCanvas("fit_canvas", "Fit Results")
xframe.Draw()
legend = R.TLegend(0.65, 0.68, 0.9, 0.86) # Specify the position of the legend (x1, y1, x2, y2)
legend.SetTextSize(0.04) 
legend.AddEntry("Data", "Data", "p")  # Add data legend entry
legend.AddEntry("PDF", "Total Fit", "l")  # Add total fit legend entry
legend.AddEntry("Signal", "Signal Fit", "l")  # Add signal legend entry
legend.AddEntry("Background", "Background Fit", "l")  # Add signal legend entry
legend.Draw()  # Draw the legend on the canvas

c.SaveAs("fit_example.pdf")

#Collapse
    