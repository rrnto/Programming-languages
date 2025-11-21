#include <stdio.h>

int main ()
{
	char car;
	
	printf("Saisie du  caractère : \n ");
	scanf("%c",&car);
	
	if ((car=='a') || (car=='e') || (car=='i') || (car=='o') || (car=='u') || (car=='y'))
	 {
	 	printf(" le variable %c est une voyelle. \n",car);
	 }
	
	else 
	printf("le variable %c est une consonne . \n", car);
	
	return 0;
}