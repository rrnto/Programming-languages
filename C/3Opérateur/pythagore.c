#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main ()
{
	float a=0, b=0;
	float c=0;
	
    printf(" \t CALCUL DE L'HYPOTÉNUSE h: \n   \t h=√(a^2 +b^2)  \n \n");
		
	printf("La valeur de a : \n");
	scanf("%f",&a);
	
	printf("La valeur de b: \n");
	scanf("%f",&b);
	
	c= sqrt (a*a +b*b);
	printf(" L' hypoténuse vaut : %.2f ",c);
	
	return 0;
}