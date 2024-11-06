#include <stdio.h>
int main(int argc,char**argv){ //a A b B P
    int A, a, B, b, P;
    scanf("%d %d %d %d %d",&A,&a,&B,&b,&P);
    if (A>P || B>P) printf("No");
    else if (A<=b) printf("Yes");
    else if (B<=a) printf("Yes");
    else if (A+B<=P) printf("Yes");
    else printf("No");
    return 0;
}