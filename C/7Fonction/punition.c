#include <stdio.h>
#include <string.h>

void punish(int lignes, char texte[ ]);

int main(int argc,char *argv[ ])
{
	signed char punition[1024];
	int rows;
	
	printf("Entrez votre punition: \n");
	scanf("%s",punition);
	printf("Combien de fois:\n");
	scanf("%d",&rows);
//	getchar( );
	punish(rows, punition);
	
	return 0;
}

void punish(int lignes ,char texte[ ])
{
	int i;
	
	for(i=1;i<=lignes;i++)
	{
		printf("%d- %s\n", i, texte);	
	}	
}