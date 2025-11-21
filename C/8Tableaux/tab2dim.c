#include <stdio.h>

int main(void)
{
    int i,j;
    int mat[3][2]={ {1,2},{3,4},{5,6} };
    
    for(i=0;i<3;i++)
         {
         	for(j=0;j<2;j++)
         	      printf("ELEMENT D'INDICE [%d][%d] = %d \n",i,j,mat[i][j]);
          }	
	
	return 0;
}