#include <stdio.h>
#include <string.h>

int main() {
    int i, j, k, x = 0, y = 0, z;
    char s;

    scanf("%d%d", &j, &i);
    char A[i][j + 1];

    for(k = 0; k < i; k++) {
        scanf("%s", A[k]);
    }

    for(z = 1; z <= i * j;) {
        if(A[x][y] == '>' || (A[x][y] == '.' && s == '>')) {
            y++; z++;
            s = '>';
            if(y >= j) break;
        } else if(A[x][y] == 'v' || (A[x][y] == '.' && s == 'v')) {
            x++; z++;
            s = 'v';
            if(x >= i) break;
        } else if(A[x][y] == '<' || (A[x][y] == '.' && s == '<')) {
            y--; z++;
            s = '<';
            if(y < 0) break;
        } else if(A[x][y] == '^' || (A[x][y] == '.' && s == '^')) {
            x--; z++;
            s = '^';
            if(x < 0) break;
        } else if(A[x][y] == '*') {
            z = 1000;
            break;
        }
    }

    if(z == 1000) printf("*\n");
    else printf("!\n");

    return 0;
}
