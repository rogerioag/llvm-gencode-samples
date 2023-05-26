#include <stdio.h>


char c[] = "c string";

int main(){

	char name[20];
	printf("%s\n", c);
	printf("Enter name: ");
	scanf("%s", name);
  printf("Your name is %s.", name);
  
	return 0;
}
