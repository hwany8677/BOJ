#include <stdio.h>
int main(){
    int buf[9];
    int res[7];
    int sigma;
    int entry=0;
    for (int i=0; i<9; i++) scanf("%d",&buf[i]);
    for (int i=0; i<9; i++){
        for (int j=i+1; j<9; j++){
            for (int idx=0; idx<7; idx++) res[idx]=0;
            sigma=0;
            entry=0;
            for (int k=0; k<9; k++){
                if (k==i || k==j) continue;
                else{
                    sigma+=buf[k];
                    res[entry]=buf[k];
                    if (sigma==100 && entry==6){
                        for (int l=0; l<7; l++) printf("%d\n",res[l]);
                        return 0;
                    }
                    entry+=1;
                }
            }
        }
    }
    return 0;
}
