#include <iostream>
#include "LexAnalysis.h"

using namespace std;

int main()
{
    lexanalysis Ex1;
    string input;
    cout<<"Please input a line of code:"<<endl;
    getline(cin, input);
    Ex1.findTokens(input);

    cout<<"\n======LEXICAL ANALYSIS REPORT======"<<endl<<endl;
    Ex1.output_id();
    Ex1.output_cons();
    Ex1.output_ops();
    Ex1.output_delim();
    Ex1.output_inv();
    Ex1.output_keyw();
    Ex1.total_token();

    return 0;
}
