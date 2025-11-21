#include<iostream>
struct node
{
    int nbr;
    node* head;
};

class builder
{
    private :
        node* adresse;
    public :
        builder()
        {
            adresse = nullptr;
        }
        //inserstion a la tete du liste
        void addaloha(int nbr)
            {
                node* vao = new node{nbr, nullptr};
                if (adresse == nullptr)
                    {
                        adresse = vao;
                    }
                else
                    {
                        vao->head = adresse;
                        adresse = vao;
                    }
            }
        //inserstion a la fin du liste
        void addarina(int nbr)
        {
            node* vao = new node{nbr, nullptr};
            if(adresse == nullptr)
                {
                    adresse = vao;
                }
            else
                {
                    node* boite = adresse;
                    while(boite->head != nullptr)
                    {
                        boite = boite->head;
                    }
                    boite->head = vao;
                }
        }
        //print ze ao anaty liste
        void display() const
        {
            node* temp = adresse;
            while (temp != nullptr) {
                std::cout << temp->nbr << " -> ";
                temp = temp->head;
            }
            std::cout << "null";
        }
};
int main()
{
    builder liste;
    liste.addaloha(10);
    liste.addaloha(20);
    liste.addaloha(30);
    liste.addarina(01);
    liste.addaloha(02);
    liste.addarina(03);

    liste.display();
    
    return 0;
}