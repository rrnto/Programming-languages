#include <stdio.h>

int main (void)
{
	int min ;
	int max ;
	int sum; 
	
	printf("Entrez un nombre MIN (1 à 1000) : \n");
	scanf("%d",&min);
	
	if(min < 1)
	 {
	 	printf(" \t ERROR \n Nombre trop petit \n ");
	 	return -1;
	 }
	 
		printf("Entrez un nombre MAX (1 à 1000) : \n");
	scanf("%d",&max);
	
	if(max>1000)
	 {
	 	printf(" /t ERROR /n Nombre trop grand \n ");
	 	return -1;
	 }
	 
	 if(min>max)
	  {
	  	printf(" \t ERROR!!!\n ");
	  	return -1;
	  }
	  
	  for(int i = min; i<max + 1; i++)
	  	sum+=i;
	  
  	printf("Somme finale :%d",sum);
	  	  	
	return 0;
}