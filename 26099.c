#include <stdio.h>
int main(int argc,char**argv){
    long long n;
    long long count;
    scanf("%lld",&n);
    if (n%5==0) printf("%lld",n/5);
    else if (n/10==0){
        if (n%3==0) printf("%lld",n/3);
        else if (n%5==0) printf("%lld",n/5);
        else if (n==8) printf("2");
        else printf("-1");
    }
    else{
        count=0;
        while(n>0){
            n-=3;
            count+=1;
            if (n%5==0){
                count+=n/5;
                printf("%lld\n",count);
                return 0;
            }
        }
        printf("-1");
    }
    printf("\n");
    return 0;
}
