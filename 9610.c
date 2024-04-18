#include <stdio.h>
int main(){
    int t,i,point[5]={0},x,y;
    scanf("%d", &t);
    for(i=0; i<t; i++){
        scanf("%d %d", &x, &y);
        if (x>0 && y>0) point[0]+=1;
        if (x<0 && y>0) point[1]+=1;
        if (x<0 && y<0) point[2]+=1;
        if (x>0 && y<0) point[3]+=1;
        if (x==0 || y==0) point[4]+=1;
    }
    for(i=0; i<4; i++) printf("Q%d: %d\n", i+1,point[i]);
    printf("AXIS: %d", point[4]);
    return 0;
}