#include <iostream>

int main()
{
    const int TAB_SIZE = 2;
    int tab[TAB_SIZE] = {1, 2};

    std::cout << tab[0] << std::endl;

    for(int i{}; i < std::size(tab); ++i)
        std::cout << tab[i] << std::endl;

    return 0;
}
// [COMPILATION]
// g++ -std=c++17 tableau.cpp -o prog.exe