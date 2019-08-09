#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int i1;
    long i2;
    char i3;
    float i4;
    double i5;

    cin >> i1;
    cout <<i1<<endl;
    cin >> i2;
    cout <<i2<<endl;
    cin >> i3;
    cout <<i3<< endl;
    cin >> i4;
    cout <<fixed;
    cout.precision(3);
    cout <<i4 << endl;
    cin >> i5;
    cout << fixed;
    cout.precision(9);
    cout <<i5 << endl;
    return 0;
}
