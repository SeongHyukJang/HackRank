#include <bits/stdc++.h>

using namespace std;

int countingValleys(int n, string s) {
    int res = 0,sea = 0;
    for(int i = 0;i<n;i++)
    {
        if(s[i] == 'U'){sea += 1;}
        else if(s[i] == 'D'){sea -= 1;}
        if(sea == 0 && s[i] == 'U'){res += 1;}
    }
    return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
