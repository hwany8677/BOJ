#include <stdio.h>
int main(int argc,char**argv){
	int i;
	char buf[81];
	fgets(buf,81,stdin);
	while(1){
		if (buf[0]=='*' && buf[1]=='*' && buf[2]=='*') break;
		for (i=0; buf[i]!='\n'; i++);
		i-=1;
		while(i>=0){
			printf("%c",buf[i]);
			i-=1;
		}
		printf("\n");
		fgets(buf,81,stdin);
	}
	return 0;
}
