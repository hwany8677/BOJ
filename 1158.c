//닭이 없으면? 꿩을 먹으면 된다!!!
#include <stdio.h>
int table[5000]={1};
int checkTable(){
    int c=0;
    int length=0;
    for (int i=0; table[i]!=0; i++) length++;
    for (int i=0; table[i]!=0; i++){
        if (!table[i]) c+=1;
        else c+=0;
    }
    if (c==length) return 0;
    else return 1;
}
int main(){
    int n,k;
    scanf("%d %d", &n, &k);
    int i=1;
    int copy_k=k-1;
    while(checkTable()){
        if (copy_k==0 && table[i-1]){
            table[i-1]=0;
            copy_k=k-1;
            printf(checkTable() ? "%d, " : "%d>", i);
            printf("%d",i);
            i=i!=n ? i+1 : 1;
            continue;
        }
        if (table[i-1]) copy_k-=1;
        i=i!=n ? i+1 : 1;
    }
    printf("\n");
}