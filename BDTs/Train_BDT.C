/******************************
Script to train a BDT for the inclusive radiative lines. List of arguments:
- signal_files: Text file with list of proxy signal files. Each file in one line
- background_files: Text file with list of proxy background files. Each file in one line
- BDTVariables: Text file with the list of BDT variables. Each variable in one line
- cutfile: File containing cuts to be applied line
- BDTName: Name given to the classifier (HHGamma, HHGammaEE, HHHGamma, HHHGammaEE)
********************************/

#include <fstream>
#include <iostream>
#include <list>
#include <string>

#include "TChain.h"
#include "TCut.h"
#include "TFile.h"
#include "TTree.h"

#include "TMVA/DataLoader.h"
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"

//Define anonymous namespace for these functions so that there is no conflict
namespace
{

  // Read lines from a file and return a list. Each entry is a line
  std::list<std::string> ReadVariables(std::string filename)
  {
    std::ifstream input;
    std::string basura = "";

    std::list<std::string> l;
    input.open(filename.c_str());

    std::getline(input, basura);
    while (basura != "")
    {
      l.push_back(basura);
      basura = "";
      std::getline(input, basura);
    }

    input.close();

    return l;
  }

  TCut ReadCuts(std::string cutfile)
  {
    // Do nothing if no cutfile has been specified
    if (cutfile == "")
      return "";
    // Open and retrieve cuts
    std::ifstream input;
    std::string basura;
    TCut cuts = "";

    input.open(cutfile.c_str());

    std::getline(input, basura);
    while (basura != "")
    {
      cuts = cuts + TCut(basura.c_str());
      basura = "";
      std::getline(input, basura);
    }

    return cuts;
  }
}

void Train_BDT(std::string signal_files, std::string background_files,
               std::string BDTVariables, std::string BDTName,
               std::string cutfile = "")
{
  // Get the lists of things
  auto signal_list = ReadVariables(signal_files);
  auto background_list = ReadVariables(background_files);
  auto BDTVars_list = ReadVariables(BDTVariables);
  auto cuts = ReadCuts(cutfile);

  // Instantiate TMVA class
  TMVA::Tools::Instance();

  // Output file to store the results
  TFile *outfile = TFile::Open(
      ("BDTs/Tuples/BDT_" + BDTName + "-results.root").c_str(), "RECREATE");

  // Decalre factory
  TMVA::Factory *factory =
      new TMVA::Factory(BDTName.c_str(), outfile,
                        "V:!Silent:Color:Transformations=I:DrawProgressBar:"
                        "AnalysisType=Classification");
  TMVA::DataLoader *dl = new TMVA::DataLoader();

  // Load signal and background into TChains (assuming here that the trees are
  // all "DecayTree")
  TChain *signal_chain = new TChain("DecayTree");
  TChain *background_chain = new TChain("DecayTree");
  for (auto &l : signal_list)
    signal_chain->Add(l.c_str());
  std::cout << "Signal chain loaded: " << signal_chain->GetEntries()
            << " entries" << std::endl;
  for (auto &l : background_list)
    background_chain->Add(l.c_str());
  std::cout << "Background chain loaded: " << background_chain->GetEntries()
            << " entries" << std::endl;

  // To avoid issues when training the BDT, we copy these inputs into trees
  // assigned to files
  TFile *signal_file = TFile::Open("BDTs/Tuples/BDTsig.root", "RECREATE");
  signal_file->cd();
  TTree *signal_tree = signal_chain->CopyTree(cuts);
  dl->AddSignalTree(signal_tree);
  TFile *background_file = TFile::Open("BDTs/Tuples/BDTbkg.root", "RECREATE");
  background_file->cd();
  TTree *background_tree = background_chain->CopyTree(cuts);
  dl->AddBackgroundTree(background_tree);

  // Load the variables
  for (auto &var : BDTVars_list)
    dl->AddVariable(var.c_str(), 'D');

  // Prepare training
  dl->PrepareTrainingAndTestTree("", "", "SplitMode=Random:SplitSeed=100");

  // TMVA method
  factory->BookMethod(dl, TMVA::Types::kBDT, "BDT",
                      "NTrees=400:MaxDepth=2:CreateMVAPdfs=True");

  // Train and test
  factory->TrainAllMethods();
  factory->TestAllMethods();
  factory->EvaluateAllMethods();
}