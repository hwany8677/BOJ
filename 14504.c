//뭐하자는 거지 ㅅㅂ
#include <stdio.h>
int main(){
    int n,m,cmd,i,j,k,count;
    int a[100000];
    int query[4];
    scanf("%d",&n);
    for(int idx=0; idx<n; idx++) scanf("%d",&a[idx]);
    scanf("%d",&m);
    for(int _=0; _<m; _++){
        for(int q=0; q<4; q++) query[q]=-1;
        scanf("%d",&cmd);
        if (cmd==1){
            for (int q=1; q<4; q++) scanf("%d",&query[q]);
            cmd=query[0];
            i=query[1]-1;
            j=query[2]-1;
            k=query[3];
            count=0;
            for (int idx=i; idx<j+1; idx++){
                if (a[idx]>k) count+=1;
            }
            printf("%d\n",count);
        }
        else{
            for (int q=1; q<3; q++) scanf("%d",&query[q]);
            cmd=query[0];
            i=query[1]-1;
            k=query[2];
            a[i]=k;
        }
    }
    return 0;
}