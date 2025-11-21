#include <stdio.h>
#include <string.h>

/*
     (*monPointeur).un_champ = x
     monPointeur -> un_champ = x
*/

typedef struct player
{
   signed char username[256];
   int hp;
   int mp;	
} joueur;

void create_player(joueur *p)
{
	strcpy(p->username, "Ranto");
	p->hp = 200;
	p->mp = 100;
}

int main(void)
{
    joueur p1= { "", 0, 0};
    
    create_player(&p1);
    	
    printf("Nom du joueur : %s \n", p1.username);
    printf("PV: %d  \t PM:%d",p1.hp ,p1.mp);	
 
    return 0;
}
