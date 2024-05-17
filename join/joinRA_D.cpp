

#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
#include "Table.h"

using namespace std;

int main() {
    std::vector<string> tables;
    for (const auto &entry: std::filesystem::directory_iterator(".")) {
        if (entry.path().string().find("outputE") != string::npos) {
            tables.push_back(entry.path().string());
        }
    }

    Table illicitDrugs = Table::fromCSV("../illicit_drugs.csv");
    vector<string> drugKeys = illicitDrugs.getColumn("inchikey");


    vector<string> stream;
    vector<string> combTableNames;


    std::cout << "combining files" << std::endl;
    for (auto &annof: tables) {
        Table anno = Table::fromTSV(annof);
        combTableNames = anno.getTableNames();
        vector<string> dataAssessions = anno.getColumn("InChIKey");
        for (int j = 0; j < dataAssessions.size(); j++) {
            for (int i = 0; i < drugKeys.size(); i++) {
                if (dataAssessions[j] == drugKeys[i]) {
                    string dhsjdhjs;
                    for (int k = 0; k < illicitDrugs[0].size(); k++) {
                        dhsjdhjs += illicitDrugs[i][k] + "\t";
                    }
                    for (int k = 0; k < anno[0].size(); k++) {
                        dhsjdhjs += anno[j][k] + "\t";
                    }
                    stream.push_back(dhsjdhjs);
                    if (stream.size() % 1000 == 0) {
                        std::cout << stream.size() << " " << j << std::endl;
                    }
                }
            }
        }
    }
    std::ofstream output;
    output.open("finaloutputE.tsv");
    string out = "";
    for (const auto &tablename: illicitDrugs.getTableNames()) {
        out += tablename + "\t";
    }
    for (const auto &tablename: combTableNames) {
        out += tablename + "\t";
    }
    out.pop_back();
    out += "\n";
    for (const auto &row: stream) {
        out += row + "\n";
    }
    output << out;
    output.close();
    return 0;
}
