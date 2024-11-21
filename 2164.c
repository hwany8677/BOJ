#include <stdio.h>
#include <math.h>
int main(int argc,char**argv){
    int n;
    scanf("%d",&n);
    int t=pow(2,(int)log2(n));
    int temp;
    if (t==n) printf("%d",t);
    else{
        temp=n-t;
        printf("%d",2*temp);
    }
    printf("\n");
    return 0;
}
