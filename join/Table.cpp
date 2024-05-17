//
// Created by Phili on 5/13/2024.
//

#include "Table.h"

vector<string> splitString(string str, char eek) {
    string substr;
    vector<string> substrs;
    for (int i =0; i < str.size(); i++) {
        if (str[i] != eek) {
            substr += str[i];
        }
        else {
            substrs.push_back(substr);
            substr = "";
        }
    }
    substrs.push_back(substr);
    return substrs;
}




Table Table::fromCSV(const string& filename) {
    std::ifstream file;
    file.open(filename);
    string fileString;
    Table ret = Table();
    while (std::getline(file, fileString)) {
        ret._data.push_back(splitString(fileString,','));
    }
    file.close();
    return ret;

}
Table Table::fromTSV(const string& filename) {
    std::ifstream file;
    file.open(filename);
    string fileString;
    Table ret = Table();
    while (std::getline(file, fileString)) {
        ret._data.push_back(splitString(fileString,'\t'));
    }
    file.close();
    return ret;
}

vector<string> Table::getTableNames() {
    return _data[0];
}

vector<vector<string>> Table::getData() {
    vector<vector<string>> ret;
    for (int i = 1; i < _data.size(); i++) {
        ret.push_back(_data[i]);
    }
    return ret;
}

vector<string> Table::getColumn(const string& col) {
    if (_data.size() == 0) {
        throw std::underflow_error("Table not initialized");
    }
    vector<string> ret;
    int columnindex = 0;
    for (int i = 0; i < _data[0].size(); i++) {
        if (_data[0][i] == col) {
            columnindex = i;
            break;
        }
    }
    ret.reserve(_data.size()-1);
    for (int i = 1; i < _data.size(); i++) {
        ret.push_back(_data[i][columnindex]);
    }
    return ret;
}

vector<string> Table::operator[](int index) {
    return _data[index+1];
}

int Table::getRowsSize() {
    return _data.size() -1;
}

int Table::getColsSize() {
    return _data[0].size();
}
