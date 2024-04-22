#include <stdio.h>
int main(){
    int n;
    int s,a;
    int left=0;
    scanf("%d", &n);
    for (int i=0; i<n; i++){
        scanf("%d %d", &s, &a);
        left+=a-s*((int)(a/s));
    }
    printf("%d", left);
    return 0;
}