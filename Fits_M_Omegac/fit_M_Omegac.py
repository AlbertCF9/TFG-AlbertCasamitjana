# lb-conda-dev virtual-env default/2024-06-23 venv_Lb2ppimumu
# . venv_Lb2ppimumu/bin/activate
import ROOT as R

R.RooMsgService.instance().setGlobalKillBelow(R.RooFit.ERROR)
R.RooMsgService.instance().setSilentMode(R.kTRUE)

R.gROOT.ProcessLine(".x lhcbStyle.C")

for i in ["LLL","DDL","DDD"]:

    tree = f"TupleOmegac2OmegaPiPiPi_{i}/DecayTree"
    root_file = f"filtered_omegac_{i}.root"

    df = R.RDataFrame(tree, root_file)

    print(df.Count().GetValue())

    df.Snapshot(tree, f"test_{i}.root", ["Omegac_M"])

    #Define the range
    x_lower = 2650
    x_upper = 2740
    x_range = R.RooRealVar("Omegac_M", "Omegac_M", x_lower, x_upper)

    #Read the data file
    data = R.TChain("ch_data")

    data.Add(f"test_{i}.root/{tree}")

    print(data.GetEntries())
    RDS_data = R.RooDataSet("a_data", "a_data",data, R.RooArgSet(x_range))
    RDS_data = RDS_data.reduce((R.RooFit.CutRange("Omegac_M")))
    entries_data = RDS_data.sumEntries()

    # Define the signal model pdf
    mean = R.RooRealVar("#mu", "mean", 2695, 2685, 2705)
    sigma = R.RooRealVar("#sigma", "sigma", 1, 0, 3.5)
    alphaL = R.RooRealVar("alphaL", "alphaL", 1, 0, 20)
    nL = R.RooRealVar("nL", "nL", 1, 0, 20)
    alphaR = R.RooRealVar("alphaR", "alphaR", 1, 0, 20)
    nR = R.RooRealVar("nR", "nR", 1, 0, 20)

    CrystalBall = R.RooCrystalBall ("CrystalBall","CrystalBall",x_range,mean,sigma,alphaL,nL,alphaR,nR)
    #Gaussian = R.RooGaussian('Gaussian', 'Gaussian', x_range, mean, sigma)

    # Define the background model pdf
    coef1 = R.RooRealVar("coef1", "coef1", 0, -1, 1)  
    coef2 = R.RooRealVar("coef2","coef2",0,-1,1)
    
    Chebychev = R.RooChebychev("Chebychev","Chebychev",x_range,R.RooArgList(coef1,coef2))
    
        # Build composite pdf
    sig_yield = R.RooRealVar("N_{sig}", "Signal yield", entries_data*0.2, 0, 1.2*entries_data)
    bkg_yield = R.RooRealVar("N_{bkg}", "Background yield", entries_data*0.8, 0, 1.2*entries_data)
    model = R.RooAddPdf("model", "model", R.RooArgList(CrystalBall, Chebychev), R.RooArgList(sig_yield, bkg_yield))

    #make the fit
    number_of_bins = 30
    results = model.fitTo(RDS_data, R.RooFit.Save(True))
    xframe = x_range.frame(R.RooFit.Title(f"Fit Result"))
    custom_binning = R.RooBinning(number_of_bins, x_lower, x_upper)


    RDS_data.plotOn(xframe, R.RooFit.Name("Data"),R.RooFit.Binning(custom_binning))  # Plot the data points
    model.plotOn(xframe, R.RooFit.LineColor(R.kBlue), R.RooFit.Name("PDF"))  # Plot the fit model
    model.plotOn(xframe, R.RooFit.Components("CrystalBall"), R.RooFit.LineColor(R.kGreen), R.RooFit.LineStyle(R.kDashed), R.RooFit.Name("Signal"))
    # Plot the Chebychev with proper scaling
    model.plotOn(xframe, R.RooFit.Components("Chebychev"), R.RooFit.LineColor(R.kRed), R.RooFit.LineStyle(R.kDashed), R.RooFit.Name("Background"))
    model.paramOn(xframe, R.RooFit.Layout(0.8, 0.99, 0.9))

    xframe.GetXaxis().SetTitle("#it{m}(" + '#Omegac'+"[MeV/#it{c}^{2}]")

    bin_width = (x_upper-x_lower)/100
    xframe.GetYaxis().SetTitle(f"Candidates/({bin_width}MeV/c^{2})")

    c = R.TCanvas("fit_canvas", "Fit Results")
    xframe.Draw()
    legend = R.TLegend(0.1, 0.75, 0.35, 0.9) # Specify the position of the legend (x1, y1, x2, y2)
    legend.SetTextSize(0.04) 
    legend.AddEntry("Data", "Data", "p")  # Add data legend entry
    legend.AddEntry("PDF", "Total Fit", "l")  # Add total fit legend entry
    legend.AddEntry("Signal", "Signal Fit", "l")  # Add signal legend entry
    legend.AddEntry("Background", "Background Fit", "l")  # Add signal legend entry
    legend.Draw()  # Draw the legend on the canvas

    c.SaveAs(f"fit_Omegac_M_{i}.pdf")

    #Collapse