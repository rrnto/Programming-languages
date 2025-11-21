#include <stdio.h>
#include <string.h>

int main(void)
{
    char nom[] = "Ranto";

    printf("avant : %s \n", nom);
    strrev(nom);
    printf("apres : %s \n", nom);

    return 0;
}