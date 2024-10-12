#include <stdio.h>
int main(){
    int precalc[9][4]={
        {0,0,0,0},
        {0,0,0,0},
        {6,2,4,8},
        {1,3,9,7},
        {0,0,0,0},
        {0,0,0,0},
        {0,0,0,0},
        {1,7,9,3},
        {6,8,4,2},
    };
    int a,b;
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; i++){
        scanf("%d %d",&a,&b);
        a%=10;
        if (a==0) printf("10");
        else if (a==1) printf("1");
        else if (a==4) printf(b%2 ? "4" : "6");
        else if (a==5) printf("5");
        else if (a==6) printf("6");
        else if (a==9) printf(b%2 ? "9" : "1");
        else printf("%d",precalc[a][b%4]);
        printf("\n");
    }
    return 0;
}