#include <iomanip>
#include <iostream>

using namespace std;

int main() {
	double matriz[12][12], soma = 0, resultado = 0;
	char o;
	cin >> o;

	for (int i = 0; i < 12; i++)
		for (int j = 0; j < 12; j++)
			cin >> matriz[i][j];

	for (int i = 0; i <= 4; i++)
		for (int j = i + 1; j <= 10 - i; j++)
			soma += matriz[j][i];

	resultado = (o == 'S' ? soma : soma / 66.0);

	cout << setprecision(1) << fixed << resultado << endl;

	return 0;
}
