#include <iostream>
#include <string>

int main()
{
    int number{0};
    std::string name{};

    std::cout << "Entrez votre âge : ";
    std::cin >> number;

    std::cout << "Comment vous appelez-vous ? : ";
    std::cin >> name;

    std::cout << "Vous avez : " << number << " ans" << std::endl;
    std::cout << "Et votre nom est : " << name << std::endl;

    return 0;
}
