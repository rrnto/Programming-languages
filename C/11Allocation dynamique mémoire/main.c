#include <stdio.h>
#include <stdlib.h>

/*
       siezeof(<donnee>) : retourne la taille en octet d'une donnée
       malloc(<taille_en_octets>) : allouer dynamiquement une zone mémoire
       free(<donnee_allouee>) : libère la mémoire allouée dynamiquement
*/

int main(void)
{
	int nombreJoueurs = 0;
	int *liste_joueurs = NULL;
	int i;
	
	printf("Combien de joueurs ?\n");
	scanf("%d",&nombreJoueurs);
	
	liste_joueurs = malloc(sizeof(int) * nombreJoueurs);
	/*
	alloué dynamiquement : liste_joueurs[nombreJoueurs]
	*/
	
	if(liste_joueurs == NULL)
	     exit(1);
	     
	for(i =0; i < nombreJoueurs; i++)
	{
		printf("Joueur %d -> numero %d\n", i + 1, i * 3);
		liste_joueurs[i] = i * 3;
	}
	
		for(i =0; i < nombreJoueurs; i++)
	{
		printf("[%d]", liste_joueurs[i]);
	}
	
	free(liste_joueurs);
	
	return 0;
}