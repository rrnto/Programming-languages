#include <stdio.h>
#include <stdlib.h>

void creer_id3( int **tab, int rows, int cols);
void afficherMatrice(int **tab, int rows, int cols);

int main(void)
{
	int **tab;
	int n = 3;
	int m = 3;
	
    creer_id3(tab, n, m);	
	afficherMatrice(tab, n, m);
	
	return 0;
}

void creer_id3(int **tab, int rows, int cols)
{
	int i, j;
	
	for(i = 0; i < rows; i++)
	{
		for(j = 0; j < cols; j++)
		{
			if(i == j)
			     tab[i][j] = 1;
			else
			     tab[i][j] = 0;
		}
	}
}

void afficherMatrice(int **tab, int rows, int cols)
{
	int i, j;
	
	for(i = 0; i < rows; i++)
	{
		for(j = 0; j < cols; j++)
		{
			printf("[%d]", tab[i][j]);
		}
		
		printf("\n");
	}
}

