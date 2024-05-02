//Hello from the future!
//Minor change from #12495396
#include <stdio.h>
int main() {
	int arr[9][9];
	int max=-1, x=0, y=0;
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &arr[i][j]);
			if (arr[i][j] >= max) {
				max = arr[i][j]; 
				x = i+1, y = j+1;
			}
		}
	}
	printf("%d\n%d %d", max, x, y);
	return 0;
}
