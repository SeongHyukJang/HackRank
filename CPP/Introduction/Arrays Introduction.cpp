#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int x;
    cin >> x;
    int arr[x];
    for(int i =0;i<x;i++)
    {
        int ele;
        cin >> ele;
        arr[i] = ele;
    }
    for(int i = x-1;i>=0;i--)
    {
        cout << arr[i] << ' ';
    }
    return 0;
}
