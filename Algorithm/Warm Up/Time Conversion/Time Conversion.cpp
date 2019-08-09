#include <bits/stdc++.h>

using namespace std;


string timeConversion(string s) {
    int hour = stoi(s.substr(0,2));
    int minute = stoi(s.substr(3,5));
    int second = stoi(s.substr(6,8));
    string x = s.substr(8,10);
    
    if(x == "PM")
    {
        hour += 12;
        if(hour == 24)
        {
            hour = 12;
        }
    }

    if((x == "AM")&&(hour == 12))
    {
        hour = 0;
    }
 
    string H,M,S;
    if(hour<10){H = "0"+to_string(hour);}
    else{H = to_string(hour);}

    if(minute<10){M = "0"+to_string(minute);}
    else{M = to_string(minute);}

    if(second<10){S = "0"+to_string(second);}
    else{S = to_string(second);}
    
    string res = H + ":" + M + ":" + S;
    return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
