#include <iostream>

/*
    <type><nom_fonction>(<type> &<valeur>): passage par réference
*/

void change_variable(int &n)
{
    n = 16;
}

/*
    surcharge de fonction
*/

int sum(int a, int b)
{
    return a + b;
}

double sum(double a, double b)
{
    return a + b;
}

int main()
{
    auto number{1};
    auto nb1{16.5};
    auto nb2{12.6};

    std::cout << "Avant nombre : " << number << std::endl;
    change_variable(number);
    std::cout << "Après nombre : " << number << std::endl;

    std::cout << sum(nb1, nb2) << std::endl;

    return 0;
}