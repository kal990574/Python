#include <iostream>
#include <string>
using namespace std;
int main() {
	int cnt = 0;
	float max = 0;
	float res = 0;
	cin >> cnt;
	float* arr = new float[cnt];
	for (int i = 0; i < cnt; i++) {
		cin >> arr[i];
		if (max < arr[i]) max = arr[i];
	}
	for (int i = 0; i < cnt; i++) {
		arr[i] = 100 * arr[i] / max;
	}
	for (int i = 0; i < cnt; i++) {
		res += arr[i];
	}
	res = res / cnt;
	cout << res;
}
//1001 1008 1152 1157 1330 1546
