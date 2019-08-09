#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N;
    cin >> N;
    vector<int> vec;
    
    int data;
    for(int i = 0;i<N;i++)
    {
        cin >> data;
        vec.push_back(data);
    }
    
    int x;
    cin >> x;
    vec.erase(vec.begin()+x-1);
    int y,z;
    cin >> y >> z;
    vec.erase(vec.begin()+y-1,vec.begin()+z-1);

    cout << vec.size()<<endl;
    for(int i = 0;i<vec.size();i++)
    {
        cout << vec[i] << " ";
    }
    return 0;
}
