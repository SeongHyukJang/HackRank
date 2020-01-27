#include <bits/stdc++.h>
using namespace std;

vector<string> split_string(string);

vector<int> waiter(vector<int> number, int q) 
{
    vector<vector<int>> B;
    vector<int> prime(q);
    prime[0] = 2;
    prime[1] = 3;
    for (int i = 5, count = 2; count < q; i++)
    {
        bool check = true;
        for (int j = 0; j < count; j++)
        {
            if (i % prime[j] == 0) { check = false; }
        }
        if (check) { prime[count++] = i; }
    }

    for(int i = 0;i<q;i++)
    {
        vector<int> tempB;
        vector<int> tempA;
        for(int j = 0; j<number.size();j++)
        {
            if(number[j] % prime[i] == 0)
            {
                tempB.push_back(number[j]);
            }
            else
            {
                tempA.push_back(number[j]);
            }
        }
        number = tempA;
        B.push_back(tempB);
    }

    vector<int> result;

    for(int count = 0;count< q ;count++)
    {
        if(count % 2 != 0)
        {
            for(int i = B[count].size()-1;i>=0;i--)
            {
                result.push_back(B[count][i]);
            }
        }
        else
        {
            for(int i = 0;i<B[count].size();i++)
            {
                result.push_back(B[count][i]);
            }  
        }
    }

    if( q % 2 == 0)
    {
        for(int i = number.size()-1;i>=0;i--)
        {
            result.push_back(number[i]);
        }
    }
    else
    {
        for(int i = 0;i<number.size();i++)
        {
            result.push_back(number[i]);
        }
    }

    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nq_temp;
    getline(cin, nq_temp);

    vector<string> nq = split_string(nq_temp);

    int n = stoi(nq[0]);

    int q = stoi(nq[1]);

    string number_temp_temp;
    getline(cin, number_temp_temp);

    vector<string> number_temp = split_string(number_temp_temp);

    vector<int> number(n);

    for (int number_itr = 0; number_itr < n; number_itr++) {
        int number_item = stoi(number_temp[number_itr]);

        number[number_itr] = number_item;
    }

    vector<int> result = waiter(number, q);

    for (int result_itr = 0; result_itr < result.size(); result_itr++) {
        fout << result[result_itr];

        if (result_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}