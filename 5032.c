#include <stdio.h>
int main(){
    int e,f,c;
    scanf("%d %d %d", &e, &f, &c);
    e=e+f;
    int count=0;
    while(1){
        if (e<c) break;
        e-=c;
        e+=1;
        count+=1;
    }
    printf("%d", count);
    return 0;
}