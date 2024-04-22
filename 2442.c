#include <stdio.h>
int main(){
    int ps_n;
    scanf("%d", &ps_n);
    int n=1;
    for (int i=0; i<ps_n; i++){
        for (int j=1; j<ps_n-i; j++) printf(" ");
        for (int k=0; k<n; k++) printf("*");
        n+=2;
        printf("\n");
    }
    return 0;
}