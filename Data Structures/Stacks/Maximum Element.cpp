#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n; cin >> n;
    int arr[100000];
    int index = 0;
    int M = 0;
    for (int i = 0; i < n; i++)
    {
        int q; cin >> q;
        if (q == 1)
        {
            int data; cin >> data;
            arr[index++] = data;
            if(data > M){M = data;}
        }
        else if (q == 2)
        {
            index--;
            if(index == 0){M = 0;}
            if(arr[index] == M)
            {
                M = 0;
                for (int j = 0; j < index; j++)
                {
                    M = M > arr[j] ? M : arr[j];
                }
            }
        }
        else
        {
            cout << M << "\n";
        }
    }
    return 0;
}