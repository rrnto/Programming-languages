#include <stdio.h>

/*
    [ DECLARATION ]
      <type> <nom>[X]
     
     [ INITIALISATION ]
       table[3] = {0, 1, 2}
       table[3] = {0}  ,affichera des 0 partout

     [ ACCES ]   
        table[X] : élément d'indice X
                         X+1ème élément        
        tableau : adresse du tableau
      *tableau : premier élêment du tableau
        *(table + X) =table[X]                  
*/

void afficher_tableau(int *tab, int taille);

int main(void)
{
	int table [3] = {1, 0, -2};
	int i;
	
	afficher_tableau(table, 3);
	 
	printf("\n \n");
	table[1] = 6;
	
	afficher_tableau(table, 3);	 
	 
	return 0;
}

void afficher_tableau(int *tab, int taille)
{
	int i;

	for(i=0;i<taille;i++)
	 {
	 	printf("[%d]",tab [i]);
	 }
}