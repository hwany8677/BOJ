//Is it cubic? Is it tetrahedral?
//tetrahedral=n(n+1)(n+2)/6, =sigma(n^2)
#include <stdio.h>
int main(int argc,char**argv){
	int real_n,n; int i;
	int j; int mx=-1;
	while (1){
		mx=0;
		scanf("%d",&real_n);
		if (real_n==0) break;
		//Try every combinations when locking 1 cubic number
		for (i=0; i*i*i<=real_n; i++){
			n=real_n;
			n-=i*i*i;
			for (j=0; (j*(j+1)*(j+2))/6<=n; j++);
			j-=1;
			if (i*i*i+(j*(j+1)*(j+2))/6>mx) mx=i*i*i+(j*(j+1)*(j+2))/6;
		}
		//Try every combinations when locking 1 tetrahedral number
		n=real_n;
		for (j=0; (j*(j+1)*(j+2))/6<=n; j++){
			n-=(j*(j+1)*(j+2))/6;
			for (i=0; i*i*i<=n; i++);
			i-=1;
			if ((j*(j+1)*(j+2))/6+i*i*i>=mx) mx=i*i*i+(j*(j+1)*(j+2))/6;
		}
		printf("%d\n",mx);
	}
	return 0;
}
