#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main() {
    // Complete the code.
    string x[10] = {"NULL","one","two","three","four","five","six","seven","eight","nine"};
    string y[2] = {"even","odd"};
    int a,b;
    cin >>a;
    cin >>b;

    if((a>=1)&&(a<=9))
    {
        if(b<=9)
        {
            for(a;a<=b;a++)
            {
                cout << x[a] <<endl;
            }
            for(a;a<=b;a++)
            {
                if(a%2 == 0)
                {
                    cout << y[0]<<endl;
                }
                else
                {
                    cout << y[1] << endl;
                }
            }
        }
        else
        {
            for(a;a<10;a++)
            {
                cout <<x[a] << endl;
            }
            for(a;a<=b;a++)
            {
                if(a%2 == 0)
                {
                    cout << y[0]<<endl;
                }
                else
                {
                    cout << y[1] << endl;
                }
            }
        }

    }

    return 0;
}
