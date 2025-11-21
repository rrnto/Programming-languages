#include <stdio.h>

int *creer_tableau(void);
void afficher_tableau(int *tab, int taille);

int main(void)
{
	int *table = creer_tableau();
	
	afficher_tableau(table, 3);
	 
	printf("\n \n");
	table[1] = -4;
	
	afficher_tableau(table, 3);	 
	 
	return 0;
}

int *creer_tableau(void)
{
	static int tableau[3];
	int i;
    
    for(i=0;i<3;i++)
        tableau[i] = i*3;
    
    return tableau;	
}

void afficher_tableau(int *tab, int taille)
{
	int i;

	for(i=0;i<taille;i++)
	 {
	 	printf("[%d]",tab [i]);
	 }
}