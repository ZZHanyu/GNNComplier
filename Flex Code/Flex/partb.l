%x COMMENT


%{
int chars = 0;
int tokens = 0;
int lines = 1;
int counters = 1;
char *kw1 = "main",*kw2="if",*kw3="else",*kw4="return",*kw5="void",*kw6="printf";
%}
%%
[a-zA-Z]+[0-9a-zA-Z_]* { 
	if (strcmp(yytext,kw1)==0 || strcmp(yytext,kw2) == 0||strcmp(yytext,kw3)==0||strcmp(yytext,kw4)==0||strcmp(yytext,kw5)==0||strcmp(yytext,kw6)==0){
			printf("%5d %10s %15s %10d\n",counters,yytext,"KeyWord",lines);
		}else{
			printf("%5d %10s %15s %10d\n",counters,yytext,"ValidIndentifier",lines);
			tokens++;
			chars += strlen(yytext);
			}
	}
[\+\*\%\=/\-\<\>] {
	printf("%5d %10s %15s %10d\n",counters,yytext,"Operater",lines);
	tokens++;
	chars += strlen(yytext);
	}
[{}()] {
	if(*yytext == '{') {
		printf("%5d %10s %15s %10d\n",counters,yytext,"LBRACES",lines);
	}else{
		if (*yytext=='}'){
			printf("%5d %10s %15s %10d\n",counters,yytext,"RBRACES",lines);
			}else{
				if (*yytext=='('){
					printf("%5d %10s %15s %10d\n",counters,yytext,"LPAREN",lines);
					}else{
					if (*yytext == ')'){
						printf("%5d %10s %15s %10d\n",counters,yytext,"RPAREN",lines);
					}
				}
		}
		chars += strlen(yytext);
	}	
}		

[0-9]+ {
	printf("%5d %10s %15s %10d\n",counters,yytext,"Contents",lines);
	chars += strlen(yytext);
}

	
"//".* { }

"/*" {BEGIN COMMENT;}

<COMMENT>"*/" {BEGIN INITIAL;}

<COMMENT>. {}
	
[ \t] { }

\n {
	chars += strlen(yytext);
	lines++;
}

[,;] { 
	printf("%5d %10s %15s %10d\n",counters,yytext,"Delimiter",lines);
}

. {
	chars += strlen(yytext);
	printf("What are you input? Are You Kidding Me???\n");
}
%%

int main(int argc, char *argv[]){
	const char *input_filename = "input";
    if (argc == 2){ 
        input_filename = argv[1];
    }   
    yyin = fopen(input_filename, "r");
    printf("%5s %10s %15s %10s\n","S. No.","Lexeme","Token","Line No.");
    yylex();
    fclose(yyin);
    return 0;
}

