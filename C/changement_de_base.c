#include <stdio.h>

int main (void)
{
	int number=0;
	
	printf("Entrez un nombre entier : \n");
	scanf("%d",&number);
	
	printf("Valeur en octal : %o\n",number);
	printf("Valeur en hexa : %X\n",number);
	
	return 0;
}