#include <iostream>
/*  
   std::cin.clear{}
   std::cin.ignore{<nombre_caracteres>, <delimiteur> -> \n}
   std::cin.getline{<flux>, <string>, <delemiteur>}
*/

int main()
{
    auto a{0};
    auto b{0};
    auto s{0};

    std::cout << "Entrez la valeur de a : ";
    std::cin >> a;

    std::cout << "Entrez la valeur de b : ";
    std::cin >> b;

    s = a + b;

    std::cout << "a + b = " << s << std::endl;

    return 0;
}