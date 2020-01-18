#include <bits/stdc++.h>

using namespace std;

string isBalanced(string s) 
{
    vector<char> vec;

    for(int i = 0;i<s.size();i++)
    {
        if(s[i] == '(' || s[i] == '{' || s[i] == '[')
        {
            vec.push_back(s[i]);
        }
        else if(s[i] == ')')
        {
            if(vec.size() == 0){return "NO";}
            if(vec[vec.size()-1] != '('){return "NO";}
            vec.pop_back();
        }
        else if(s[i] == '}')
        {
            if(vec.size() == 0){return "NO";}
            if(vec[vec.size()-1] != '{'){return "NO";}
            vec.pop_back();
        }
        else if(s[i] == ']')
        {
            if(vec.size() == 0){return "NO";}
            if(vec[vec.size()-1] != '['){return "NO";}
            vec.pop_back();
        }
    }
    if(vec.size() != 0){return "NO";}
    return "YES";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string s;
        getline(cin, s);

        string result = isBalanced(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}