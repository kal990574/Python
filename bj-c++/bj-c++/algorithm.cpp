#include <iostream>
#include <string>
using namespace std;
int main() {
	string str;
	int cnt = 0;
	getline(cin, str);
	for (int i = 0; i < str.length(); i++) 
	{
		if (i == 0 || i == str.length() - 1) continue;
		if (str[i] == ' ') cnt++;
	}
	cnt += 1;
	cout << cnt;
}
//1001 1008 1152
