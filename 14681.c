#include <stdio.h>
int main(){
    int x,y;
    scanf("%d", &x);
    scanf("%d", &y);
    if (x>0) printf("%d", y>0 ? 1 : 4);
    else printf("%d", y>0 ? 2 : 3);
    return 0;
}