#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int simpleHash(const string& password) {
    int hashValue = 0;
    for (char c : password) {
        hashValue += static_cast<int>(c);
    }
    return hashValue;
}

void createHashedPasswordFile() {
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

    ofstream passwordFile("hashed_value.txt");
    if (passwordFile.is_open()) {
        for (const string& password : passwords) {
            int hashedPassword = simpleHash(password);
            passwordFile << hashedPassword << endl;
        }
        passwordFile.close();
        cout << "Hashed password file created successfully." << endl;
    } else {
        cout << "Unable to create hashed password file." << endl;
    }
}

int main() {
    createHashedPasswordFile();
    return 0;
}
