#include <stdio.h>
#include <stdlib.h>

int main ()
{  
   /*
       && : et
        | |  : ou
         !   : not
    
     
       
       if(!a) : a est fausse
       if(a) : a est vraie

     */
       
	int a = 0;
	
	printf(" Quel est votre nombre ? \n ");
	scanf("%d", &a);
	
	if(a>0)
 	 { 
	    printf(" Le nombre est positif \n ");
 	 }
   else if( a== 0)
       { 
         printf("Le nombre est nul \n ");
       }
    else
      {
      	printf(" Le nombre est négatif \n");	 
      }
      
     return 0;
}
	