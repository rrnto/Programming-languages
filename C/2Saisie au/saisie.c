#include <stdio.h>
#include <stdlib.h>

int main (void)
{
	int a = 0;
	
	printf("Quel age avez-vous ? \n");
	scanf("%d" ,  &a);
	
	printf("Vous avez %d ans. \n", a);
	
	return 0;
}