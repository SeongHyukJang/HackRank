#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t; cin >> t;
    vector<int> PushStack;
    vector<int> PopStack;

    int input, data;
    for (; t > 0; t--)
    {
        cin >> input;
        if (input == 1)
        {
            cin >> data;
            PushStack.push_back(data);
        }
        else if (input == 2)
        {
            if (PopStack.size() != 0)
            {
                PopStack.pop_back();
            }
            else
            {
                for (int i = PushStack.size()-1; i >=0; i--)
                {
                    PopStack.push_back(PushStack[i]);
                }
                PushStack.clear();
                PopStack.pop_back();
            }
        }
        else
        {
            if(PopStack.size() != 0){ cout << PopStack[PopStack.size() - 1] << endl; }
            else
            {
                for (int i = PushStack.size() - 1; i >= 0; i--)
                {
                    PopStack.push_back(PushStack[i]);
                }
                PushStack.clear();
                cout << PopStack[PopStack.size() - 1] << endl;
            }
        }
    }

    return 0;
}