#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,q;
    cin >> n >> q;
    vector<vector<int>> VEC;
    vector<int> vec;
    for(int count = 0;count<n;count++)
    {
        int size;
        cin >> size;
        int data;

        for(int i = 0;i<size;i++)
        {
            cin >> data;
            vec.push_back(data);
        }
        

        VEC.push_back(vec);

        vec.clear();
    }
    for(int c = 0;c <q;c++)
    {
    int q1,q2;
    cin >> q1 >> q2;
    cout << VEC[q1][q2]<<endl;
    }
    return 0;
}
