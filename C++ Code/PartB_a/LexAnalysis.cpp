//
// Part of function definition
// Created by Zhao Hanyu on 2022/11/3.
//

#include <iostream>
#include <string>
#include "LexAnalysis.h"
using namespace std;

//Code comments and references should be eliminated before lexical analysis,
//otherwise lexical analysis will treat the lexemes in comments as tokens!
string lexanalysis::comment_eliminate(string strs) {
    //  1.    Double quote "..." elimination
    if(strs.find('\"') != -1)
    {
        start = strs.find('"');
        end = strs.find('"',start+1);
        strs.erase(start-1,end-start+2);
        return strs;
    }else{
        //  2.  /* ... */ eliminate
        if(strs.find("/*") != -1){
            start = strs.find("/*");
            end = strs.find("*/");
            strs.erase(start-2,end-start+4);
            return strs;
        }else{
            //  3.  double slash //... eliminate
            if(strs.find("//") != -1){
                start = strs.find("//");
                end = strs.find('\n');
                strs.erase(start,end-start);
                return strs;
            }
        }
    }
    return strs;
}

int lexanalysis::ValidDelimiter(char ch)
{
    if(ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ';' || ch == '='|| ch == '<' ||ch =='>' || ch == ',')
        return 1;
    else if(ch == '(' || ch == ')'|| ch == '{' || ch=='}')
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

int lexanalysis::ValidIdentifier(string strs)
{
    if(!((strs[0] >= 'a' && strs[0] <= 'z') || (strs[0] >= 'A' && strs[0] <= 'Z') || strs[0] == '_'))
        return 0;

    for(int i = 1; i < strs.size(); i++)
    {
        if(!((strs[i] >= 'a' && strs[i] <= 'z') || (strs[i] >= 'A' && strs[i] <= 'Z') || (strs[i] >= '0' && strs[i] <= '9') || strs[i] == '_'))
            return 0;
    }
    return 1;
}

int lexanalysis::ValidConstant(string strs)
{
    int i, len = strs.size();

    if(len == 0)
        return 0;

    for(i=0; i<len; i++)
    {
        if((strs[i] != '0' && strs[i] != '1' && strs[i] != '2' && strs[i] != '3' && strs[i] != '4' && strs[i] != '5' && strs[i] != '6' && strs[i] != '7' && strs[i] != '8' && strs[i] != '9' || strs[i] == '-' && i>0))
            return 0;
    }
    return 1;
}

int lexanalysis::ValidKeyword(string strs)
{
    if(strs == "for" || strs == "if" || strs == "else if" || strs == "else" || strs == "while" || strs == "do" || strs == "return" || strs == "int" || strs == "float" || strs == "bool" || strs == "char" || strs == "double" || strs=="printf" || strs=="main")
        return 1;
    return 0;
}

string lexanalysis::subString(string strs, int left, int right)
{
    string subs = strs.substr(left, right - left + 1);
    return subs;
}

int lexanalysis::get_count() const {
    return count;
}

int lexanalysis::get_lines() const {
    return lines;
}

void lexanalysis::lines_plus() {
    lines++;
}

void lexanalysis::count_plus() {
    count ++;
}

void lexanalysis::findTokens(string strs)
{
    int left=0, right=0;    //  used to locate substrings
    int length = strs.size();

    //stop when right index exceeds string length
    while(right <= length && left <= right)
    {
        if(ValidDelimiter(strs[right]) == 0)
            right++;
        if(ValidDelimiter(strs[right]) != 0 && left == right)
        {
            if(ValidOperator(strs[right]) == 1)
            {
                count_ops++;
                count_plus();   //  token counter
                ops[count_ops] = strs[right];
                printf("%5d %10c %20s %10d\n",get_count(),strs[right],"Operator",get_lines());
            }
            else if(ValidDelimiter(strs[right]) != 3)
            {
                delim[count_delim] = strs[right];
                //Determine the specific type of separator (left bracket? right bracket?)
                if (strs[right] == '('){
                    printf("%5d %10c %20s %10d\n",get_count(),strs[right],"LPAREN",get_lines());
                }else{
                    if (strs[right] == ')'){
                        printf("%5d %10c %20s %10d\n",get_count(),strs[right],"RPAREN",get_lines());
                    }else{
                        if(strs[right] == '{'){
                            printf("%5d %10c %20s %10d\n",get_count(),strs[right],"LBRACE",get_lines());
                        }else{
                            if(strs[right]=='}'){
                                printf("%5d %10c %20s %10d\n",get_count(),strs[right],"RBRACE",get_lines());
                            }
                        }
                    }
                }
                count_delim++;
                count_plus();
            }
            right++;
            left = right;
        }
        else if(ValidDelimiter(strs[right]) != 0 && left != right || (right == length && left != right))
        {
            string subs = subString(strs, left, right-1);

            if(ValidConstant(subs) == 1 && ValidDelimiter(strs[right]) != 2)
            {
                cons->append(subs);
                count_plus();
                printf("%5d %10s %20s %10d\n",get_count(),subs.c_str(),"Constant",get_lines());
            }
            else if(ValidKeyword(subs) == 1 && ValidIdentifier(subs) == 1)
            {
                keyw->append(subs);
                printf("%5d %10s %20s %10d\n",get_count(),subs.c_str(),"Keyword",get_lines());
                count_plus();
            }
            else if(ValidKeyword(subs) == 0 && ValidIdentifier(subs) == 1)
            {
                id->append(subs);
                printf("%5d %10s %20s %10d\n",get_count(),subs.c_str(),"Identifier",get_lines());
                count_plus();
            }
            else if(ValidIdentifier(subs) == 0)
            {
                inv->append(subs);
                printf("%5d %10s %20s %10d\n",get_count(),subs.c_str(),"InValid_Identifier",get_lines());
                count_plus();
            }
            left = right;
        }
    }
}


