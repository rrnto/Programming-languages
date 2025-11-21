#include <stdio.h>
#include <string.h>

int main (void)
{
	char prenom[5] = "Aina";
	char stockage[256 ] ;
	
	printf("Ton prénom de base : %s \n",prenom);
	
	printf("Changer ton prénom ?\n ");  
	scanf("%s ", stockage);
	
	strcpy(prenom, stockage);
	
	printf("Ton nouveau prénom : %s \n",prenom);
	
	return 0;
}
	
	