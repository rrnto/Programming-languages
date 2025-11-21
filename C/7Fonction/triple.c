#include <stdio.h>

int triple(int a);

int main(int argc, char **argv)
{
	int nombre;
	
	printf("Entrez un nombre: \n");
	scanf("%d",&nombre);
	printf("Le triple de %d est %d", nombre, triple(nombre));
	
	return 0;
}

int triple(int a)
{
	return a * 3;
}