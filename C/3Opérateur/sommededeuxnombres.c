#include <stdio.h>
#include <stdlib.h>

int main ()
{  
    /* 
         == : égale à
          != : différent de
           < : plus petit que
           > : plus grand que
         <= : plus petit ou égale à
         >= : plus grand ou égale à
	
    */	
	
	
	int a = 0, b = 0;
	int s;
	
	printf(" \t CALCULATRICE \n \n ");
	printf(" Valeur de a : \n");
	scanf("%d", &a);
	printf(" Valeur de b : \n");
	scanf("%d", &b);
	
	s=a+b;
	printf(" a + b = %d \n", s);
	
	return 0;
}