//
// Created by Zhao Hanyu on 2022/11/3.
//
#include <iostream>
#include <string>
#include "LexAnalysis.h"
using namespace std;

int lexanalysis::ValidDelimiter(char ch)
{
    if(ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ';' || ch == '=')
        return 1;
    else if(ch == '(' || ch == ')')
        return 2;
    else if(ch == ' ')
        return 3;
    return 0;
}

int lexanalysis::ValidOperator(char ch)
{
    if(ch == '=' || ch == '+' || ch == '-' || ch == '*' || ch == '/')
        return 1;
    return 0;
}

int lexanalysis::ValidIdentifier(string str)
{
    if(!((str[0] >= 'a' && str[0] <= 'z') || (str[0] >= 'A' && str[0] <= 'Z') || str[0] == '_'))
        return 0;

    for(int i = 1; i < str.size(); i++)
    {
        if(!((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z') || (str[i] >= '0' && str[i] <= '9') || str[i] == '_'))
            return 0;
    }
    return 1;
}

int lexanalysis::ValidConstant(string str)
{
    int i, len = str.size();

    if(len == 0)
        return 0;

    for(i=0; i<len; i++)
    {
        if((str[i] != '0' && str[i] != '1' && str[i] != '2' && str[i] != '3' && str[i] != '4' && str[i] != '5' && str[i] != '6' && str[i] != '7' && str[i] != '8' && str[i] != '9' || str[i] == '-' && i>0))
            return 0;
    }
    return 1;
}

int lexanalysis::ValidKeyword(string str)
{
    if(str == "for" || str == "if" || str == "else if" || str == "else" || str == "while" || str == "do" || str == "return" || str == "int" || str == "float" || str == "bool" || str == "char" || str == "double")
        return 1;
    return 0;
}

string lexanalysis::subString(string str, int left, int right)
{
    string subs = str.substr(left, right - left + 1);
    // cout<<subs<<endl;
    return subs;
}

void lexanalysis::findTokens(string str)
{
    int left=0, right=0;
    int length = str.size();

    while(right <= length && left <= right)
    {
        if(ValidDelimiter(str[right]) == 0)
            right++;
        if(ValidDelimiter(str[right]) != 0 && left == right)
        {
            if(ValidOperator(str[right]) == 1)
            {
                ops[count_ops] = str[right];
                count_ops++;
            }
            else if(ValidDelimiter(str[right]) != 3)
            {
                delim[count_delim] = str[right];
                count_delim++;
            }
            right++;
            left = right;
        }
        else if(ValidDelimiter(str[right]) != 0 && left != right || (right == length && left != right))
        {
            string subs = subString(str, left, right-1);

            if(ValidConstant(subs) == 1 && ValidDelimiter(str[right]) != 2)
            {
                cons[count_cons] = subs;
                count_cons++;
            }
            else if(ValidKeyword(subs) == 1 && ValidIdentifier(subs) == 1)
            {
                keyw[count_keyw] = subs;
                count_keyw++;
            }
            else if(ValidKeyword(subs) == 0 && ValidIdentifier(subs) == 1)
            {
                id[count_id] = subs;
                count_id++;
            }
            else if(ValidIdentifier(subs) == 0)
            {
                inv[count_inv] = subs;
                count_inv++;
            }
            left = right;
        }
    }
}

void lexanalysis::output_id() {
    int len=0;
    cout<<"=====Identifiers:====="<<endl;
    cout<<"Total: "<<count_id<<endl;
    while(len <= count_id)
    {
        cout<<id[len]<<endl;
        len++;
    }
}

void lexanalysis::output_cons() {
    int len = 0;
    cout<<"=====Constants:====="<<endl;
    cout<<"Total: "<<count_cons<<endl;
    while(len <= count_cons)
    {
        cout<<cons[len]<<endl;
        len++;
    }
}

void lexanalysis::output_ops() {
    int len=0;
    cout<<"=====Operators:====="<<endl;
    cout<<"Total: "<<count_ops<<endl;
    while(len <= count_ops)
    {
        cout<<ops[len]<<endl;
        len++;
    }
}

void lexanalysis::output_delim() {
    int len=0;
    cout<<"=====Delimiters:====="<<endl;
    cout<<"Total: "<<count_delim<<endl;
    while(len <= count_delim)
    {
        cout<<delim[len]<<endl;
        len++;
    }
}

void lexanalysis::output_inv() {
    int len=0;
    cout<<"=====Keywords:====="<<endl;
    cout<<"Total: "<<count_keyw<<endl;
    while(len <= count_keyw)
    {
        cout<<keyw[len]<<endl;
        len++;
    }
}

void lexanalysis::output_keyw() {
    int len=0;
    cout<<"=====Invalid Identifiers:====="<<endl;
    cout<<"Total: "<<count_inv<<endl;
    while(len <= count_inv)
    {
        cout<<inv[len]<<endl;
        len++;
    }
}

void lexanalysis::total_token() {
    cout<<"Total number of tokens: "<<count_cons+count_delim+count_id+count_inv+count_ops+count_keyw<<endl;
}