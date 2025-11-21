#include<stdio.h>
int main()
{
	int a,i,j,c;
	puts("Table de multiplication de:");
	scanf("%d",&a);
	puts("Jusqu'à :");
	scanf("%d",&i);
	for(j=1;j<=i;j++)
	{
		c=a*j;
		printf("%d x %d = %d\n",a,j,c);
	}
}