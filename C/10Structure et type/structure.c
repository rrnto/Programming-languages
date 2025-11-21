#include <stdio.h>

struct player
{
   signed char username[256];
   int hp;
   int mp;	
};

int main(void)
{
    struct player p1= { "Aina", 100, 100};
    
    printf("Nom du joueur : %s \n", p1.username);
    printf("PV: %d  \t PM:%d \n",p1.hp ,p1.mp);	
 
    return 0;
}
