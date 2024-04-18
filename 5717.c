#include <stdio.h>
int main(){
    int l=0,r=0;
    while(1){
        scanf("%d %d", &l, &r);
        if (l==0 && r==0) break;
        printf("%d\n",l+r);
    }
    return 0;
}