// Main Function
// Made by Zhao Hanyu
// This function is mainly used to get user input and pass it to the lexical analyzer.

//  Other parts of this program:
//      1.  Variable/function declaration, please move to "LexAnalysis.h"
//      2.  Function definition, please move to "LexAnalysis.cpp"
//
//  Development environment:
//      System version: MacOS 13.0.1 (22A400)
//      Platform: Intel X86 (Quad Core Intel Core i5 with 8GB RAM)
//      Compiler: CLion 2022.1
//

#include <iostream>
#include <string>
#include "LexAnalysis.h"

using namespace std;

lexanalysis Ex1;

int main()
{
    string input;
    cout<<"Input you code here: "<<endl;

    //  Continue to get input until a row is empty
    while(getline(cin,input))
    {
        Ex1.lines_plus();   //lines counter
        if(input=="\n"){    //skip newlines
            continue;
        }else {
            if (Ex1.get_lines() == 1) { //print header ONLY on first loop
                printf("\n%5s %10s %20s %10s\n", "S.No", "Lexeme", "Token", "Line No.");
            }
            //Eliminate comments/references before code is passed to the lexer
            string strs(Ex1.comment_eliminate(input));
            Ex1.findTokens(strs);   //Start lexical analysis line by line
        }
    }

    return 0;
}
