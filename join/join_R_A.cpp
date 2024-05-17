#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <filesystem>
#include "Table.h"

using namespace std;


int main() {
    std::vector<string> tables;
    for (const auto & entry : std::filesystem::directory_iterator("../spectrum_annotaties")) {
        tables.push_back(entry.path().string());
    }

    Table samples = Table::fromTSV("../ReDU_filtered_envirement.tsv");
    std::cout << "read files" << std::endl;
    vector<string> annoRows;
    vector<string> sampleAssessions = samples.getColumn("filename");
    vector<string> tmp;
    for (const auto & sampleAssession : sampleAssessions) {
        auto tmpp = splitString(sampleAssession,'.');
        auto ttt = tmpp[1] + "." + tmpp[2];
        tmp.push_back(ttt);
    }

    int i = 0;
    for (auto & annof : tables) {
        Table anno = Table::fromTSV(annof);
        i++;
        vector<string> dataAssessions = anno.getColumn("full_CCMS_path");
        for (int j = 0; j < dataAssessions.size(); j++) {
            for (int i = 0; i < tmp.size(); i++) {
                if (dataAssessions[j] == tmp[i]) {
                    string dhsjdhjs;
                    for (int k=0; k < samples[0].size(); k++) {
                        dhsjdhjs += samples[i][k] + "\t";
                    }
                    for (int k=0; k < anno[0].size(); k++) {
                        dhsjdhjs += anno[j][k] + "\t";
                    }
                    annoRows.push_back(dhsjdhjs);
                    if (annoRows.size() % 1000 == 0) {
                        std::cout << annoRows.size() << " " << j << std::endl;
                    }
                }
            }
        }
        std::ofstream output;
        output.open("outputE" + to_string(i) + ".tsv");
        string out = "";
        for (const auto & tablename : samples.getTableNames()) {
            out += tablename + "\t";
        }
        for (const auto & tablename : anno.getTableNames()) {
            out += tablename + "\t";
        }
        out.pop_back();
        out += "\n";
        for (const auto & annoRow : annoRows) {
            out+=  annoRow + "\n";
        }
        output << out;
        output.close();
        annoRows.clear();
    }
    return 0;
}
