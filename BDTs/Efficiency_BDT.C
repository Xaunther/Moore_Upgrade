/******************************
Script to get the BDT efficiency for different cuts of the BDT. List of parameters
- files: File with the list of files to process
- BDTVariables: Files with list of BDT Variables
- BDTName: Name of the BDT to load
- N_cuts: Number of cuts between -1 and 1 to try.
********************************/

#include <string>
#include <list>
#include <vector>
#include <fstream>

#include "TChain.h"
#include "TBranch.h"
#include "TMVA/Reader.h"
#include "TMVA/Tools.h"

#define BDTmin -1
#define BDTmax 1

//Define anonymous namespace for these functions so that there is no conflict
namespace
{

    // Read lines from a file and return a list. Each entry is a line
    std::list<std::string> ReadVariables(const std::string &filename)
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

    //Retrieve entries for each fiven BDT cut
    std::list<std::pair<double, double>> GetEntriesForEachCut(const std::list<double> &BDT_response, const int &N_cuts)
    {
        std::list<std::pair<double, double>> results;
        //Current cut
        double cut = BDTmin;
        //Loop on the ordered list
        int k = BDT_response.size();
        for (const auto &r : BDT_response)
        {
            if (r > cut) // If the current value is above the cut
            {
                results.push_back({cut, k}); //Save this cut with its result
                cut += double(BDTmax - BDTmin) / double(N_cuts + 1);
            }
            k--;
        }
        //Add last cut, which corresponds to BDT_response>1
        results.push_back({1, 0});

        return results;
    }
}
void Efficiency_BDT(const std::string files, const std::string outputfile, const std::string BDTVariables, const std::string BDTName, const int N_cuts = 100)
{
    //Get list of input files
    auto file_list = ReadVariables(files);
    auto BDTVars_list = ReadVariables(BDTVariables);

    //Load the TChain
    TChain *file_chain = new TChain("DecayTree");
    for (auto &l : file_list)
        file_chain->Add(l.c_str());

    //Instance TMVA READER
    TMVA::Tools::Instance();
    TMVA::Reader *reader = new TMVA::Reader("V:Color:!Silent");

    //Link reader to array of floats (input)
    std::vector<float> vars_float(BDTVars_list.size());
    std::vector<double> vars_double(BDTVars_list.size());

    int i = 0;
    for (auto &v : BDTVars_list)
    {
        reader->TMVA::Reader::AddVariable(v.c_str(), &vars_float[i]);
        file_chain->SetBranchAddress(v.c_str(), &vars_double[i]);
        i++;
    }

    //TMVA method
    //The Folder is the one used by default
    reader->TMVA::Reader::BookMVA("BDT method", ("default/weights/" + BDTName + "_BDT.weights.xml").c_str());

    //List with the BDT outputs
    std::list<double> BDT_response;

    //Time to loop on tree entries
    for (long k = 0; k < file_chain->GetEntries(); k++)
    {
        //Some output to see it's still alive
        if (k % 100000 == 0)
            std::cout << "--- ... Processing event: " << k << std::endl;

        file_chain->GetEntry(k);

        //Pass the variables retrieved (in double format) to float (needed by the reader)
        for (unsigned int j = 0; j < BDTVars_list.size(); j++)
            vars_float[j] = vars_double[j];
        BDT_response.push_back(reader->TMVA::Reader::EvaluateMVA("BDT method"));
    }

    //We can now order the BDT_response to increase speed from this point forward
    BDT_response.sort();

    //Finally, get the number of entries passing each cut. N_cuts is the number of cuts tried, which are equally spaced between -1 and 1
    auto results = GetEntriesForEachCut(BDT_response, N_cuts);

    //Save into file
    std::ofstream outf;
    outf.open(outputfile.c_str());
    for (auto &result : results)
        outf << "BDT_response > " << result.first << " | " << result.second << std::endl;
    outf.close();
}
