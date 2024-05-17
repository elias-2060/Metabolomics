//
// Created by Phili on 5/13/2024.
//

#ifndef UNTITLED1_TABLE_H
#define UNTITLED1_TABLE_H
#include <iostream>
#include <fstream>
#include <deque>
#include <vector>

using namespace std;

vector<string> splitString(string str, char eek);


class Table {
private:
    std::deque<std::vector<std::string>> _data;

    Table() {}

public:
    static Table fromCSV(const string& filename);

    static Table fromTSV(const string& filename);

    vector<string>getTableNames();

    vector<vector<string>> getData();

    vector<string> getColumn(const string& col);

    vector<string> operator[](int index);

    int getRowsSize();

    int getColsSize();

};

#endif //UNTITLED1_TABLE_H
