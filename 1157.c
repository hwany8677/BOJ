//Updated code
#include <stdio.h>
int main(){
    char str[1000001];
    int alpha_c[26]={0};
    scanf("%s",str);
    for (int i=0; str[i]!=0; i++){
        if (str[i]>96) alpha_c[str[i]-97]++;
        else alpha_c[str[i]-65]++;
    }
    int mx=0;
    for (int i=0; i<26; i++){
        if (alpha_c[i]>mx) mx=alpha_c[i];
    }
    int has_mx=0;
    int loc=0;
    for (int i=0; i<26; i++){
        if (mx==alpha_c[i]){
            if (has_mx) {
                printf("?");
                return 0;
            }
            has_mx=1;
            loc=i;
        }
    }
    printf("%c",loc+65);
    return 0;
}