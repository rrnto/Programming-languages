#include <stdio.h>

int main ()
{
	int a,b,r;
	
	printf(" \t PGCD(a,b) \n \n");
	printf(" appuyer sur entree pour commencer \n \n");
    getchar();
    
    printf("valeur de a : \n ");
    scanf("%d",&a);
    
    printf("valeur de b : \n");
    scanf("%d",&b);
    
    r = a%b;
    
    while ( r != 0)
       {
       	a=b;
       	b=r;
       	r=a%b;
        }
   
       printf("PGCD(a,b) : %d",b);
       
       return 0;
}