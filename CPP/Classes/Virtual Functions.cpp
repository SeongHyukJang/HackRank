#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person
{
protected:
    string name;
    int age;
    int count;
public:
    virtual void getdata() = 0;
    virtual void putdata() = 0;

};

class Professor : public Person
{
private:
    int publications;
    static int cur_id;
public:
    void getdata() override
    {
        cin >> this->name >> this->age >> this->publications;
        cur_id++;
        this->count = cur_id;
    }
    void putdata() override
    {
        cout << this->name << ' ' << this->age << " " << this->publications << ' ' << this->count << endl;
    }
};

class Student : public Person
{
private:
    int marks[6];
    static int cur_id;
public:
    void getdata() override
    {
        cin >> this->name >> this->age;
        for (int i = 0; i < 6; i++)
        {
            cin >> this->marks[i];
        }
        cur_id++;
        this->count = cur_id;
    }
    void putdata() override
    {
        cout << this->name << ' ' << this->age << ' ';
        int sum = 0;
        for (int i = 0; i < 6; i++)
        {
            sum += marks[i];
        }
        cout << sum << ' ' << this->count << endl;
    }
};

int Professor::cur_id = 0;
int Student::cur_id = 0;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}