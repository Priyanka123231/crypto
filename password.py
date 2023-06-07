#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
void createPasswordFile() {
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
    ofstream passwordFile("passwords.txt");
    if (passwordFile.is_open()) {
        for (const string& password : passwords) {
            passwordFile << password << endl;
        }
        passwordFile.close();
        cout << "Password file created successfully." << endl;
    } else {
        cout << "Unable to create password file." << endl;
    }
}

int main() {
    createPasswordFile();
    return 0;
}
