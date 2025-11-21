#include <iostream>

/*
[INITIALISATION]
    <type> <nom_variable>{valeur}
    <auto> <nom_variable>{valeur}: Déduction de type

Constante : cont <type> <NOM>{valeur}

[FONCTION DE DEDUCTION DE TYPE]
    dectype(auto) <nom>
*/

int main()
{
    int someData1 = 14;
    int someData2(18);
    int someData3{20};

    std::cout << someData1 << std::endl;
    std::cout << someData2 << std::endl;
    std::cout << someData3 << std::endl;

    return 0;
}