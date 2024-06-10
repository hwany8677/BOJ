#include <stdio.h>
int main(){
    int a,b,c;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    char res[20];
    sprintf(res,"%lld",(long long int)a*b*c);
    int count[10]={0};
    for (int i=0; res[i]!=0; i++)count[res[i]-48]++; 
    for (int i=0; i<10; i++) printf("%d\n", count[i]);
    return 0;
}