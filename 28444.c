#include <stdio.h>
int main(){
    int h,i,a,r,c;
    scanf("%d %d %d %d %d",&h,&i,&a,&r,&c);
    int res1=0,res2=0;
    res1=h*i;
    res2=a*r*c;
    printf("%d\n",res1-res2);
    return 0;
}