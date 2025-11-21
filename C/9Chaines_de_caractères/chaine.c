#include <stdio.h>

int main (void)
{
	signed char mot[ 26] ;
	
	printf(" Comment tu t'appelles ? : \n");
	scanf("%s",mot);
	
	printf("Tu t'appelles : %s",mot);
	
	return 0;
}