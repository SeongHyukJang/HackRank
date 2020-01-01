#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
	int T; cin >> T;
	cout << setiosflags(ios::uppercase);
	cout << setw(0xf) << internal;
	while(T--) {
		double A; cin >> A;
		double B; cin >> B;
		double C; cin >> C;
        cout << hex << nouppercase << left << showbase << (long long) A << endl;
        cout << dec << right << setw(15) << setfill('_') << showpos << fixed << setprecision(2) << B << endl;
        cout << noshowpos << setprecision(9) << uppercase << scientific << C << endl;
	}
	return 0;
}