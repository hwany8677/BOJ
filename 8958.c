#include <stdio.h>
int main(){
    int t;
    scanf("%d", &t);
    int i;
    for (i=0; i<t; i++){
        char s[80];
        scanf("%s", s);
        int sc=0,stk=0;
        int j;
        for (j=0; s[j]!=0; j++){
            if (s[j]=='O') {stk+=1; sc+=stk;}
            else stk=0;
        }
        printf("%d\n",sc);
    }
    return 0;
}