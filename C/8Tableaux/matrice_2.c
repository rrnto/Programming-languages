#include <stdio.h>

const rows = 2, cols = 2;

int main(int argc, char **argv)
{
	int i, j;
	int A[ ][ ] = {{1,0},{0,1}};
	
	for(i = 0; i < rows; i++)
	{
		for(j = 0; j < cols; j++)
		{
			printf("[%d]", A[ i ][ j ]);
		}
		
		printf("\n");
	}
	
	return 0;
}