#include<stdio.h>
int main()
{
	int p,i,n;
	i=0;
	scanf("%d",&n),
	printf("\n\n");
	while(i<n)
	{
		i++;
		p=rand()%10;
		printf("m=%d \n",p);
	}
}