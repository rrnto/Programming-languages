#include<iostream>


int main()
{
    auto a{0};
    auto b{0};
    auto s{0};

    std::cout << "La valeur de a : ";
    std::cin >> a;
    
    std::cout << "La valeur de b : ";
    std::cin >> b;
    
    s = a + b;
    
    std::cout << "a + b = " << s << std::endl;

    return 0;
}