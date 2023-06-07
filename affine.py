#include <iostream>
using namespace std;

int gcdExtended(int a, int b, int* x, int* y) {
    if (a == 0) {
        *x = 0;
        *y = 1;
        return b;
    }

    int x1, y1;
    int gcd = gcdExtended(b % a, a, &x1, &y1);

    *x = y1 - (b / a) * x1;
    *y = x1;

    return gcd;
}

int modInverse(int a, int m) {
    int x, y;
    int gcd = gcdExtended(a, m, &x, &y);
    if (gcd != 1) {
        cout << "Error: Modular inverse does not exist.";
        return -1;
    }
    return (x + m) % m;
}

string affineEncrypt(string plaintext, int a, int b) {
    string ciphertext = "";
    int m = 26; // Assuming 26 characters in the alphabet

    for (char c : plaintext) {
        if (isalpha(c)) {
            char encryptedChar = ((a * (c - 'a') + b) % m) + 'a';
            ciphertext += encryptedChar;
        } else {
            ciphertext += c;
        }
    }

    return ciphertext;
}

string affineDecrypt(string ciphertext, int a, int b) {
    string plaintext = "";
    int m = 26; // Assuming 26 characters in the alphabet
    int aInverse = modInverse(a, m);

    for (char c : ciphertext) {
        if (isalpha(c)) {
            char decryptedChar = ((aInverse * ((c - 'a') - b + m)) % m) + 'a';
            plaintext += decryptedChar;
        } else {
            plaintext += c;
        }
    }

    return plaintext;
}

int main() {
    
    string plaintext ;
    cout<<"Enter the plaintext to produce ciphertext"<< endl;
    cin >> plaintext;
    int a = 5; // Multiplicative key
    int b = 8; // Additive key

    string ciphertext = affineEncrypt(plaintext, a, b);
    cout << "Ciphertext: " << ciphertext << endl;

    string decryptedText = affineDecrypt(ciphertext, a, b);
    cout << "Decrypted Text: " << decryptedText << endl;

    return 0;
}
