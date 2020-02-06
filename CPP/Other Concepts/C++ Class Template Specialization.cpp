#include <iostream>
using namespace std;
enum class Fruit { apple, orange, pear };
enum class Color { red, green, orange };

template <typename T> struct Traits;
static int i = 0;

template <typename T>
struct Traits
{
    static string name(int index);
};

template <typename T>
string Traits<T>::name(int index)
{
    string res;
    if (i % 2 ==  0)
    {
        if (index == 0) { res =  "red"; }
        else if (index == 1) { res =  "green"; }
        else if (index == 2) { res =  "orange"; }
        else { res =  "unknown"; }
    }
    else
    {
        if (index == 0) { res = "apple"; }
        else if (index == 1) { res = "orange"; }
        else if (index == 2) { res = "pear"; }
        else { return "unknown"; }
    }
    i++;
    return res;
}

int main()
{
	int t = 0; std::cin >> t;

    for (int i=0; i!=t; ++i) {
        int index1; std::cin >> index1;
        int index2; std::cin >> index2;
        cout << Traits<Color>::name(index1) << " ";
        cout << Traits<Fruit>::name(index2) << "\n";
    }
}