#include <stdio.h>
#include<stdlib.h>

/*
	[COMPILATION]
		gcc <nom_du_fichier> -o <nom_de_l'executable>
		<appeler l'executable>
*/

int main()
{
	int a = 25, b =175;
	int i,j ;
	char car='E' , f='e' ;
	i=22;
	j=i;
	
	printf("vous avez %d ans et vous mesurez %d cm \n", a, b);
	printf ("i vaut %d \n", i);
	printf ("i+j vaut %d \n", i+j);
	printf("car=%c f=%c", car, f);
	
	return 0;
}