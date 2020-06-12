void getvars(string filename, string outputfile, string treename = "DecayTree")
{
  TFile* file = TFile::Open(filename.c_str());
  TTree* tree = (TTree*)file->Get(treename.c_str());

  ofstream outf;
  outf.open(outputfile.c_str());
  for (int i = 0; i < tree->GetListOfLeaves()->GetEntries(); i++)
    {
      outf << (*tree->GetListOfLeaves())[i]->GetName() << endl;;
    }
  outf.close();
}
