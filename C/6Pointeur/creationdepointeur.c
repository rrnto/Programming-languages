#include <stdio.h>

/*
    [POINTEUR]
    
    *pointeur = 0 ou *pointeur = &ma variable (déclaration et initialisation d'un pointeur)

    pointeur : adresse de la variable pointée
 
   *pointeur : valeur de la variable pointée

    &pointeur : adresse du pointeur
  
*/

void inverser_nombres(int *p_a, int *p_b)
{
	int temporaire=0;
	
	temporaire = *p_b;
	*p_b =*p_a;
	*p_a = temporaire;
}

int main (void)
{
    int A=15, B=28;
    
    int *pointeurSurA = &A;
    int *pointeurSurB = &B;
		
	printf("Avant : A = %d et B = %d \n",A,B);
	inverser_nombres(pointeurSurA, pointeurSurB);
	printf("Après : A = %d et B = %d",A ,B);
	
	return 0;
}