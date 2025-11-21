#include <stdio.h>

void creerMatrice(int mat[3][3], int *a)
{
	mat[0][0] = *a;
}

void afficherMatrice(int mat[3][3], int n)
{
	int i, j;
	
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < n; j++)
		{
			printf("[%d]", mat[i][j]);
		}
		
		printf("\n");
	}
}

int main(void)
{
	int matA[3][3];
	int n = 3;
	int a;
	
	printf("Matrice 3*3:\n\n");
	printf(" \n");
	printf("Entrer votre matrice\n\n");
	printf("Valeur de a:\n");
	scanf("%d", &a);
	
	creerMatrice(matA, &a);
	afficherMatrice(matA, n);
	
	return 0;
}