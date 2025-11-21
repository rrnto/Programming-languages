#include <stdio.h>

void afficher_matrice(float **tab, int rows, int cols);

int main(int argc, char **argv)
{
	float a, b, c, d;
	float detA;
	float **matriceA;
	
	matriceA[ 0 ][ 0 ] = 2;
	matriceA[ 1 ][ 0 ] = 4;
	matriceA[ 1 ][ 1 ] = 6;
	matriceA[ 0 ][ 1 ] = 0;
	
	afficher_matrice( matriceA, 2, 2);
	
	return 0;
}

void afficher_matrice(float **tab, int rows, int cols)
{
	int i, j;
	
	for(i = 0; i < rows; i++)
	{
		for(j = 0; j < cols; j++)
		{
			printf("[%d]", tab[ i ][ j ]);
		}
		
		printf("\n");
	}
}