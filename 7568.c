//동아리활동 때문에 C로 다시작성 (거의복붙)
#include <stdio.h>
int main(int argc,char**argv){
    int n;
    scanf("%d",&n);
    int info_x[n],info_y[n];
    int pos[n]; //<< pos[n]={0}으로 초기화할려다가 실패함 (GCC가 뜯어말림)
    for (int i=0; i<n; i++) {
        scanf("%d %d",&info_x[i],&info_y[i]);
        pos[i]=0;
    }
    int cur_x,cur_y;
    int comp_x,comp_y;
    for (int i=0; i<n; i++){
        cur_x=info_x[i];
        cur_y=info_y[i];
        for (int j=0; j<n; j++){
            if (i==j) continue;
            comp_x=info_x[j];
            comp_y=info_y[j];
            if (cur_x<comp_x && cur_y<comp_y) pos[i]+=1;
        }
    }
    for (int i=0; i<n; i++) printf("%d ",pos[i]+1);
    printf("\n");
    return 0;
}
