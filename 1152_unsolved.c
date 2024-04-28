#include <stdio.h>
int main(){
    char s[11]; //1 million + 1 (because of null character)
    fgets(s,11,stdin);
    int c=0;
    for (int i=0; s[i]!=10; i++){
        if (s[i]==32 && s[i+1]!=10 && i!=0) c++;
    }
    printf("%s\n\n",s);
    for (int i=0; s[i]!=0; i++) printf("%d ",s[i]);
    c++;
    printf("\n\n%d",c);
    return 0;
}