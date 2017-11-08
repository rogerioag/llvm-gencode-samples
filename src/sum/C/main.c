#include <stdio.h>

extern int sum(int x, int y);

int main(){
	int a = 12;
	int b = 30;
	int res = sum(a,b);
	printf("res: %d\n", res);
	return 0;
}
