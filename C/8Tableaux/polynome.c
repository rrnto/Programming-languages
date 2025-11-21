#include <stdio.h>
#include <math.h>

void creer_matrice(int mat[3][3], int *a,int *b, int *c, int *d, int *e, int *f, int *g, int *h, int *k);
void afficher_matrice(int mat[3][3], int n);
void creer_polynome_caracteristique(int *a,int *b, int *c, int *d, int *e, int *f, int *g, int *h, int *k);


int main(void)
{
    int a, b, c, d, e, f, g, h, k;
    int n = 3;
    int matA[3][3];

    creer_matrice(matA, &a, &b, &c, &d, &e, &f, &g, &h, &k);
    afficher_matrice(matA, n);
    creer_polynome_caracteristique(&a, &b, &c, &d, &e, &f, &g, &h, &k);

    return 0;
}

void creer_matrice(int mat[3][3], int *a,int *b, int *c, int *d, int *e, int *f, int *g, int *h, int *k)
{
    printf("Matrice 3*3 :\n");
    printf("\t\t [a][d][g] \n \t\t [b][e][h] \n \t\t [c][f][k] \n");
    printf("\n\n");
    printf("Entrez votre matrice:\n");


    printf("La valeur de a: ");
    scanf("%d", a);

    printf("La valeur de b: ");
    scanf("%d", b);

    printf("La valeur de c: ");
    scanf("%d", c);

    printf("La valeur de d: ");
    scanf("%d", d);

    printf("La valeur de e: ");
    scanf("%d", e);

    printf("La valeur de f: ");
    scanf("%d", f);

    printf("La valeur de g: ");
    scanf("%d", g);

    printf("La valeur de h: ");
    scanf("%d", h);

    printf("La valeur de k: ");
    scanf("%d", k);

    mat[0][0] = *a;
    mat[1][0] = *b;
    mat[2][0] = *c;
    mat[0][1] = *d;
    mat[1][1] = *e;
    mat[2][1] = *f;
    mat[0][2] = *g;
    mat[1][2] = *h;
    mat[2][2] = *k;

    printf("\n\n");
}

void afficher_matrice(int mat[3][3], int n)
{
    int i, j;
    n = 3;

    printf("Votre matrice A est:\n");

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            printf("[%d]", mat[i][j]);
        }

        printf("\n");
    }

    printf("\n");
}

void creer_polynome_caracteristique(int *a,int *b, int *c, int *d, int *e, int *f, int *g, int *h, int *k)
{
    int a1, b1, c1, d1;

    a1 = -1;
    b1 = *a + *e + *k;
    c1 = (*f)*(*h) - (*a)*(*e) - (*a)*(*k) - (*e)*(*k) + (*d)*(*b) + (*g)*(*c);
    d1 = (*a)*(*c)*(*k) - (*a)*(*f)*(*h) - (*d)*(*b)*(*k) + (*c)*(*d)*(*h) + (*g)*(*b)*(*f) - (*g)*(*c)*(*e);

    printf("Le polynôme caractéristique de A est: \n");
    printf("P_A(X) = -X^3 + (%d)X^2 + (%d)X + (%d) ", b1, c1, d1);
}