#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <ctime>
using namespace std;

string generateSalt() {
    const string chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    const int saltLength = 10;
    random_device rd;
    mt19937 generator(rd());
    uniform_int_distribution<int> distribution(0, chars.length() - 1);

    string salt;
    for (int i = 0; i < saltLength; i++) {
        salt += chars[distribution(generator)];
    }
    return salt;
}

string simpleHash(const string& password, const string& salt) {
    string saltedPassword = password + salt;

    int hashValue = 0;
    for (char c : saltedPassword) {
        hashValue += static_cast<int>(c);
    }
    return to_string(hashValue);
}

void createSaltedHashedPasswordFile() {
    vector<string> passwords = {
        "password1",
        "password2",
        "password3",
        "password4",
        "password5",
        "password6",
        "password7",
        "password8",
        "password9",
        "password10"
    };

    ofstream passwordFile("salted_hashed_passwords.txt");
    if (passwordFile.is_open()) {
        for (const string& password : passwords) {
            string salt = generateSalt();
            string hashedPassword = simpleHash(password, salt);
            passwordFile << password << ":" << salt << ":" << hashedPassword << endl;
        }
        passwordFile.close();
        cout << "Salted hashed password file created successfully." << endl;
    } else {
        cout << "Unable to create salted hashed password file." << endl;
    }
}

int main() {
    createSaltedHashedPasswordFile();
    return 0;
}
