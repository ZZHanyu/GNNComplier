//
// Created by Zhao Hanyu on 2022/11/3.
//

#ifndef CNN_COMPILER_LEXANALYSIS_H
#define CNN_COMPILER_LEXANALYSIS_H
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class lexanalysis{
public:
    int ValidDelimiter(char ch);
    int ValidOperator(char ch);
    int ValidIdentifier(string str);
    int ValidConstant(string str);
    int ValidKeyword(string str);
    string subString(string str, int left, int right);
    void findTokens(string str);

    void output_id();
    void output_cons();
    void output_ops();
    void output_delim();
    void output_inv();
    void output_keyw();
    void total_token();

protected:
    string id[10], cons[10], ops[10], delim[10], inv[10], keyw[10];
    int count_id = 0, count_cons = 0, count_ops = 0, count_delim = 0, count_inv = 0, count_keyw = 0;

};

#endif //CNN_COMPILER_LEXANALYSIS_H
