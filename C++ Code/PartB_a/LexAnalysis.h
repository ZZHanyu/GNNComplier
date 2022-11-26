//
// Created by Zhao Hanyu on 2022/11/3.
// This header file is a declaration of the methods required by the lexical analyzer, which contains
//      1. Token type determination method
//      2. Comment Eliminator
//      3. Intra-class reference method
//  Go to the "LexAnalysis.cpp" file for its definition
//

#ifndef CNN_COMPILER_LEXANALYSIS_H
#define CNN_COMPILER_LEXANALYSIS_H
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class lexanalysis{
protected:
    //  Define protected variables:
    int count = 1,lines = 0,count_ops = 0,count_delim = 0;
    string id[100], cons[100], ops[100], delim[100], inv[100], keyw[100];
    int start = 0,end = 0;

public:
    void findTokens(string str);    //Lexical analyzer's Ontology

    string subString(string str, int left, int right);  //Method: intercept string substring
    string comment_eliminate(string strs);  //Comment | Reference Eliminator

    int ValidDelimiter(char ch);    //Judgment separator
    int ValidOperator(char ch);     //judgment operator
    int ValidIdentifier(string str);    //judgment identifier
    int ValidConstant(string str);  //Judgment constant
    int ValidKeyword(string str);   //Judgment keywords

    //The following declares some methods to access and modify variables defined in the class
    void count_plus();  //  token counter
    int get_count() const;
    void lines_plus();  //  lines counter
    int get_lines() const;
};

#endif //CNN_COMPILER_LEXANALYSIS_H
