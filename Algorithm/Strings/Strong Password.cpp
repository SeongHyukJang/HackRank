#include <bits/stdc++.h>

using namespace std;

int minimumNumber(int n, string password) {
    int res = 0;
    int size = password.size();
    bool num = false, lower = false, upper = false,special = false;
    for(int i = 0;i<n;i++)
    {
        if(isupper(password[i])){ upper = true; }
        else if(islower(password[i])){ lower = true;}
        else if(isdigit(password[i])){num = true;}
        else{special = true;}
    }
    if(num == false) { res += 1; size +=1;}
    if(lower == false){res += 1; size +=1;}
    if(upper == false){res += 1; size +=1;}
    if(special == false){res += 1; size +=1;}
    
    if(6>size){res += 6-size;}

    return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string password;
    getline(cin, password);

    int answer = minimumNumber(n, password);

    fout << answer << "\n";

    fout.close();

    return 0;
}
