#include <stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int star=2*n-1;
    star=2*n-1;
    for (int i=0; i<n; i++){
        for (int j=0; j<i; j++) printf(" ");
        for (int k=0; k<star; k++) printf("*");
        star-=2;
        printf("\n");
    }
    return 0;
}