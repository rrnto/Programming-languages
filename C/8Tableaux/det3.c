#include <stdio.h>

void matrice_manager(int mat[3][3]);
void creer_matrice(int mat[3][3], int *a, int *b, int *c, int *d, int *e, int *f, int *g, int *h, int *i);

int main(void)
{
	int A[3][3];
	
	return 0;
}

void matrice_manager(int mat[3][3])
{
	int n;
	int a11, a12, a13;
	int a21, a22, a23;
	int a31, a32, a33;
	
	creer_matrice(mat, &a11, &a21, &a31, &a12, &a22, &a32, &a13, &a23, &a33);
}

void creer_matrice(int mat[3][3], int *a, int *b, int *c, int *d, int *e, int *f, int *g, int *h, int *i)
{
	printf("La valeur de a11 :\n");
	scanf("%d", a);
	
	printf("La valeur de a21 :\n");
	scanf("%d", b);
	
	printf("La valeur de a31 :\n");
	scanf("%d", c);
	
	printf("La valeur de a12 :\n");
	scanf("%d", d);
	
	printf("La valeur de a22 :\n");
	scanf("%d", e);
	
	printf("La valeur de a23 :\n");
	scanf("%d", f);
	
	printf("La valeur de a31 :\n");
	scanf("%d", g);
	
	printf("La valeur de a23 :\n");
	scanf("%d", h);
	
	printf("La valeur de a33 :\n");
	scanf("%d", i);
}
