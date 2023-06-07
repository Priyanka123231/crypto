 #include <iostream>
using namespace std;

int simpleHash(const string& message) {
    int hashValue = 0;
    for (char c : message) {
        hashValue += static_cast<int>(c);
    }
    return hashValue;
}

int main() {
    string message = "Hello, world!";
    int originalHash = simpleHash(message);

    cout << "Original Message: " << message << endl;
    cout << "Original Hash: " << originalHash << endl;

    // Simulate receiver
    int receivedHash = simpleHash(message);
        cout << "Recived Hash: " << receivedHash << endl;


    if (receivedHash == originalHash) {
        cout << "Data integrity verified. Hash matches." << endl;
    } else {
        cout << "Data integrity compromised. Hash does not match." << endl;
    }

    return 0;
}
