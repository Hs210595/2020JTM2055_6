%{
#include <stdio.h>
#include <stdbool.h>
int comment_lines = 0;
bool in_comment = false;
%}

%%

";".* { ++comment_lines; }
[a-z] fprintf(yyout,yytext[0] - ('a' - 'A'));
.* { 
    if (in_comment) {
    ++comment_lines;
    } else {
    fprintf(yyout, yytext);  
    }
}

%%

int yywrap() {
    return 1;
}

int main(void) {
    printf("Enter input file: ");
    yyin = fopen("input.c", "r");

   
    yyout = fopen("out.c", "w");

    yylex();
    printf("Number of comments: %d\n", comment_lines);
}
