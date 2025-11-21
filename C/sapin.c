#include <stdio.h>
#include <stdlib.h>

int main () 
{
   int i;
   int j;
   
   for (i=1; i<=10; i++) 
   {
      for (j=0;j<10-i;j++) // les espaces...
         printf(" ");
  
      for (j=0; j<(i*2-1); j++)
         printf("*");
       
       printf("\n");
    }
    
      return 0;
}