#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int size;
    cin >> size;

    vector<int> vec;
    int data;
    for(int i = 0; i<size;i++)
    {
        cin >> data;
        vec.push_back(data);
    }
    vector<int>::iterator it;
    int q;
    cin >> q;
    int q2;
    for(int i = 0;i<q;i++)
    {
        cin >> q2;
        it = lower_bound(vec.begin(),vec.end(),q2);

        if(vec[it-vec.begin()]==q2)
        {
            cout << "Yes " << distance(vec.begin(),it)+1 << endl;
        }
        else
        {
            cout << "No " << distance(vec.begin(),it)+1 << endl;
        }
    }

    return 0;
}
