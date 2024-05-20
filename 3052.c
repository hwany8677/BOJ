//피곤한와중에 소스코드가 틀린이유를 찾는데 그 이유는 break가 아닌 continue를 넣어야 했는 것이었고
//난 그걸 1시간이나 넘게 허비했다는것에 너무나 큰 허무함이 든다
#include <stdio.h>
int main(){
    int n[10];
    int i,j,temp;
    for (i=0; i<10; i++){
        scanf("%d", &temp);
        n[i]=temp % 42;
    } 
//    for (i=0; i<10; i++) printf("%d ",n[i]);
//    printf("\n");
    int dupe[11] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
    int skip=0,k=0;
    for (i=0; i<10; i++){
        skip=0;
//        printf("Currently seeking: index no. %d\n",i);
        for (j=0; dupe[j]!=-1; j++){
            if (dupe[j]==n[i]){
//                printf("Duplicate. Skipping.\n");
                skip=1;
                break;
            }
        }
        if (skip) continue;
        else {
//            printf("Appended\n");
            dupe[k]=n[i];
            k++;
        }
    }
    for (i=0; dupe[i]!=-1; i++); 
//    for (j=0; j<10; j++) printf("%d ", dupe[j]);
    printf("%d",i);
    return 0;
}