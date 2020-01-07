#include <bits/stdc++.h>

using namespace std;

int camelcase(string s) {
    int res = 1;
    for(int i = 0;i<s.size();i++)
    {
        if(isupper(s[i])){res += 1;}
    }
    return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = camelcase(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
