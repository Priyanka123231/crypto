#include <iostream>
using namespace std;

int extendedEuclidean(int a, int b, int* x, int* y) {
    if (b == 0) {
        *x = 1;
        *y = 0;
        return a;
    }

    int x1, y1;
    int gcd = extendedEuclidean(b, a % b, &x1, &y1);

    *x = y1;
    *y = x1 - (a / b) * y1;

    return gcd;
}

int multiplicativeInverse(int a, int m) {
    int x, y;
    int gcd = extendedEuclidean(a, m, &x, &y);
    if (gcd != 1) {
        cout << "Error: Modular inverse does not exist.";
        return -1;
    }

    // Ensure the result is positive
    int inverse = (x % m + m) % m;
    return inverse;
}

int main() {
    int number = 7;
    int modulo = 26;

    int inverse = multiplicativeInverse(number, modulo);
    cout << "Multiplicative Inverse: " << inverse << endl;

    return 0;
}
