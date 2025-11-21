#include <stdio.h>

#define LI 7

void creer_tab_title(char **table, int li);
void afficherTab(char **tab, int nb);

int main(void)
{
	char **tab ;
	char lundi[2];
	char mardi[3];
	char mercredi[3];
	char jeudi[5];
	char vendredi[1];
	char samedi[1];
	
	creer_tab_title(tab, LI);
	
	return 0;
}

void creer_tab_title(char **table, int li)
{
	char
	
	table[0][0] = ' ' ;
	table[0][1] ='TYPE';
	table[0][2] = 'UE, ECUE' ;
	table[0][3] = 'DUREE' ;
	table[0][4] = 'SALLE' ;
	
	table[1][0] = 'LUNDI' ;
	table[2][0] = 'MARDI' ;
	table[3][0] = 'MERCREDI' ;
	table[4][0] = 'JEUDI' ;
	table[5][0] = 'VENDREDI' ;
	table[6][0] = 'SAMEDI' ;
	
	afficherTab(table, li);
}

void afficherTab(char **tab, int *nb)
{
	int i, j;
	
	for(i = 0; i < nb; i++)
	{
		for(j = 0; j < nb; j++)
		{
			printf("[%s]", tab[i][j]);
			
			if(j = 6)
			{
				break;
			}
		}
		
		printf("\n");
	}
}
