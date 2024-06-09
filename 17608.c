//파이썬이 시간걸린다고? C로 하면되지 머!
#include <stdio.h>
int main(){
    int n,stick[100000]={0};
    scanf("%d", &n);
    int count=1;
    int m=0;
    int i;
    for (i=0; i<n; i++) scanf("%d", &stick[i]);
    for (i=0; i<n; i++) if (stick[i]>=m) m=stick[i];
    int face=stick[i-1];
    for (i=n-1; i>-1; i--){
        if (stick[i]>face) {
            count++;
            face=stick[i];
            if (stick[i]==m) break;
        }
    }
    printf("%d",count);
    return 0;
}