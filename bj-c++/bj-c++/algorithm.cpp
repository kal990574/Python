#include <iostream>
#include <string>
using namespace std;
int main() {
	string str;
	getline(cin, str);
	int max = 0;
	int cnt = 0;
	int check = 0;
	int arr[26] ={0,}; // 0~25, 대문자 차이 32
	for (int i = 0; i < str.length(); i++) {
		if (str[i] > 96) arr[str[i] - 97]++;
		else arr[str[i] - 65]++;
	}
	for (int i = 0; i < 26; i++) {
		if (max < arr[i]) {
			max = arr[i];
			check = i;
		}
	}
	for (int i = 0; i < 26; i++) {
		if (max == arr[i]) cnt++;
	}
	if (cnt > 1) cout << "?";
	else cout << char(check + 65);
}
//1001 1008 1152 1157
