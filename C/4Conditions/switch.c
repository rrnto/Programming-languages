#include <stdio.h>
#include <stdlib.h>

int main ()
{
	int a = 0;
	
	printf("Quel âge as tu? \n");
	scanf("%d",&a);
	switch(a)
	{
		case 0:
		   printf("tu n'es pas né \n");
		   break;
	
		case 15:
		   printf("tu es un enfant \n");
		   break;
		   
		case 100:
		   printf( "tu es un adulte \n");
		   break;
		   
	 default:
	       printf("zombie \n ");
	       break;
	}
	return 0;
}	 