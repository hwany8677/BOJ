#include <stdio.h>
int main(){
    int n,s;
    scanf("%d %d",&n,&s);
    int buf[20000];
    for (int i=0; i<n; i++) scanf("%d",&buf[i]);
    int count=0;
    int a,b;
    for (int i=0; i<n; i++){
        for (int j=i+1; j<n; j++){
            a=buf[i];
            b=buf[j];
            if (a+b<=s) count+=1;
        }
    }
    printf("%d\n",count);
    return 0;
}