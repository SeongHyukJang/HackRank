#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    int Q;
    cin >> Q;
    int x,mark;
    string student;
    map<string, int> m;
    map<string, int>::iterator it;
    for(int i = 0; i<Q;i++)
    {
        cin >> x;
        if(x == 1)
        {
            cin >> student >> mark;
            it = m.find(student);
            if(it == m.end()){m[student] = mark;}
            else{m[student] += mark;}
        }
        else if(x == 2)
        {
            cin >> student;
            m.erase(student);
        }
        else
        {
            cin >> student;
            cout << m[student] <<endl;
        }
    } 
    return 0;
}
