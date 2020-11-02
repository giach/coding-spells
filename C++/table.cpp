#include<iostream>
using namespace std;

// calculeaza id-ul scaunului opus fata de y
int opus(int y, int n) {
    int dy; 
    if (y <= n / 2)
        dy = y + n / 2;
    else
        dy = y - n / 2;
    return dy;
}

// calculeaza indexul scaunului tinand
// cont ca masa este rotunda, iar valoarea
// trebuie sa fie rotita
int rotatie(int valoare, int n) {
    if (valoare > n)
        return valoare - n;

    return valoare;
}

int urmator_y(int y, int k, int n, int v[]) {
    int tmp = y;

    // numara k copii de la y
    while(k > 1) {
        if (v[tmp] != -1) {
            k--;
        }
        tmp = rotatie(tmp + 1, n);
    }

    // daca dupa ce s-au numarat k copii,
    // scaunul este liber, incrementeaza
    // pana cand se gaseste un scaun ocupat
    while (v[tmp] == -1)
        tmp = rotatie(tmp + 1, n);

    return tmp;
}

void print_v(int v[], int n) {
    for(int i = 1; i <= n; i++)
        cout << v[i] << " ";
    cout << endl;
}

int main() {
    int x = 2, k = 4, n = 10;
    // int x = 7, k = 8, n = 16; 
    int v[n+1];
    int i, y, dy, id;

    v[0] = -1;
    for(i = 1; i <= n; i++) {
        v[i] = i;
    }

    y = x;
    do {
        // cauta urmatorul y care  nu a fost eliminat
        y = y + k - 1;
        dy = opus(y, n);
        cout << "y = " << y << " ; dy = " << dy << endl;
        cout << v[y] << " " << v[dy] << endl;

        for(i = y; i < n; i++) {
            v[i] = v[i + 1];
        }
        print_v(v, n-1);
        for (i = dy - 1; i < n; i++){
            v[i] = v[i + 1];
        }

        print_v(v, n-2);


       n = n - 2;
    } while(n > 2);

    cout << "castigatorii sunt: " << v[1] << "si " << v[2];
    cout << endl;

    return 0;
}