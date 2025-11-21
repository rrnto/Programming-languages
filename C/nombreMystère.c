#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 100
#define MIN 1

//const MAX =100, MIN= 1;

int main(void)
{
	int a, nombreMystere;
	int coups = 0;

	srand(time(NULL));
    nombreMystere = (rand() % (MAX - MIN + 1)) + MIN;

    while(a!=nombreMystere)
    {    printf("Quel est le nombre mystère ? \n");
         scanf("%d",&a);
                 
         if(a<nombreMystere)
             printf("C'est plus \n \n");
             
         else if(a>nombreMystere)
             printf("C'est moins \n \n");
                         
         else
             printf("Bravo !! Vous avez trouvé le nombre mystère : %d \n",nombreMystere);
             
         coups++;
     }   
     
     printf("En %d coups",coups);
	
	return 0;
}