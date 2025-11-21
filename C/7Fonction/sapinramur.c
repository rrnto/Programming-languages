#include <stdio.h>

void ramure(int clignes);
void tronc(int pos_t);

int main(void)
{
   int nb_lig;

   printf("Entrer un nombre: ");
   scanf("%d", &nb_lig);
   
   ramure(nb_lig);
   tronc(nb_lig-2);
	
	return 0;
}

void ramure(int clignes)
{
	int i=0;
	int j=0;
	
	for(i=1;i<=clignes;i++)
       {
              for(j=0;j<clignes-i;j++)
                  printf(" ");
                 
              for(j=0;j<(2*i-1);j++)
                  printf("*");
                  
           printf("\n");	
        }	
}

void tronc(int pos_t)
{
	int i=0, j=0;
	
	for(j=1;j<=3;j++)
	  {
	        for(i=1;i<=pos_t;i++)
	             printf(" ");
	           
	         printf("@@@ \n");
	  }
}