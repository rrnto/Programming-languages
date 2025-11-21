#include<stdio.h>

/*
    *tab --> tab[ ]
*/

void afficher_tableau(int *tab, int taille);

int main(void)
{
    int tableau[5]={1,5,2,6,0};
    
    afficher_tableau(tableau,5);
    
    printf("\n \n");
    tableau[3]=2;
    
    afficher_tableau(tableau,5);
		
	return 0;
}

void afficher_tableau(int *tab, int taille)
{
    int i;
    
    for(i=0;i<taille;i++)
         printf("[%d] ", tab[i]);	
}
