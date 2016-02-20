#include <iomanip>
#include <iostream>

using namespace std;

int main() {

	int c;
	double matriz[12][12], soma = 0, resultado = 0;
	char t;
	cin >> c >> t;

	for (int i = 0; i < 12; i++)
		for (int j = 0; j < 12; j++)
			cin >> matriz[i][j];

	for (int i = 0; i < 12; i++)
		soma += matriz[i][c];

	resultado = (t == 'S' ? soma : soma / 12.0);
	cout << setprecision(1) << fixed << resultado << endl;

	return 0;
}
