#include <stdio.h>
#include <string.h>

/*
     (*mon_pointeur).un_champ = X
     mon_pointeur -> un_champ = X
*/

typedef struct Player
{
	signed char username[256];
	int hp;
	int mp;
} Player;

void create_player(Player *p)
{
   strcpy((*p).username, "Ranto");
   p->hp=100;
   (*p).mp=200;	
}

int main(void)
{
    Player p1={"",0,0};	
    
    create_player(&p1);
    
    /*
        [tableau de structure]
           Player tableau_joueur[5];
           
           tableau_joueur[0].mp=150;
           tablrau_joueur[2].mp=75;
    */
    
    printf("Nom du joueur: %s \n", p1.username);
    printf("PV: %d  |  PM: %d \n", p1.hp, p1.mp);
	
	return 0;
}