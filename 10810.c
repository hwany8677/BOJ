#include <stdio.h>
int main(){
    int n,m;
    int i,j,k;
    int ball[100]={0};
    scanf("%d %d",&n,&m);
    for (int l=0; l<m; l++){
        scanf("%d %d %d",&i,&j,&k);
        for (int idx=i; idx<=j; idx++) ball[idx-1]=k;
    }
    for (int idx=0; idx<n; idx++) printf("%d ",ball[idx]);
    printf("\n");
    return 0;
}