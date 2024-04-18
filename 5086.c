//I have no idea what '//' equivalent is in C so I wrote on my own
// '//' = (a%b)*b
#include <stdio.h>
int main(){
    int a=-1, b=-1;
    while(1){
        scanf("%d %d", &a, &b);
        if (a==0 && b==0) break;
        if (a%b==0 || b%a==0){
            if ((a/b)*b!=0) printf("multiple\n");
            else if ((b/a)*a!=0) printf("factor\n");
        }
        else printf("neither\n");
    }
    return 0;
}