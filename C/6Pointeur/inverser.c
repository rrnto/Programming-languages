#include <stdio.h>

void inverser_nombres(int *a, int *b)
{
	int temporaire=0;
	
	temporaire = *b;
	*b =*a;
	*a = temporaire;
}

int main (void)
{
    int a=15, b=28;
		
	printf("Avant : a = %d et b = %d \n",a,b);
	inverser_nombres(&a, &b);
	printf("Après : a = %d et b = %d",a ,b);
	
	return 0;
}