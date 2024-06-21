#include <stdio.h>
int main(){
    while(1){
        int n;
        scanf("%d", &n);
        if (n==0) break;
        int bowl[50];
        int i;
        for (i=0; i<n; i++) scanf("%d", &bowl[i]);
        long long count=0;
        i=0;
        int j;
        int sum=50000;
        while(sum!=0){
            if (bowl[i]==0) { 
                i=0; 
                continue; 
            }
            if (i==0){
                bowl[i]=bowl[i]>0 ? bowl-1 : 0;
                count+=1;
            }
            else {
                if (bowl[i]>0) {
                    bowl[i]-=1;
                    for (j=0; j<i; j++) bowl[j]+=1;
                    count++;
                }
            }
            i=i+1<n ? i+1 : 0;
            for (j=0; j<n; j++) sum+=bowl[j];
        }
        printf("%lld\n",count);
    }
    return 0;
}