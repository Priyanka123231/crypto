#include <iostream>
#include <cmath>
//using namespace std;

// Function to calculate the modular exponentiation (base^exponent mod modulus)
long long int modExp(long long int base, long long int exponent, long long int modulus) {
    long long int result = 1;
    base = base % modulus;

    while (exponent > 0) {
        if (exponent % 2 == 1)
            result = (result * base) % modulus;

        base = (base * base) % modulus;
        exponent = exponent / 2;
    }

    return result;
}

int main() {
    // Public parameters
    long long int p ; 
  std::cout<<"enter prime number \n";
    std::cin >> p;
    
    long long int g ; 
     std::cout<<"enter generator \n";
    std::cin >> g ;
    
    // Prime number
      // Generator

    // Private keys
    long long int x ;
    
     std::cout<<"enter party A's private key \n";
    std::cin >> x ;
    
    // Party A's private key
    long long int y ;  // Party B's private key
    std::cout<<"enter party B's private key \n";
    std::cin >> y ;

    // Public key calculation
    long long int A_pub = modExp(g, x, p);  // Party A's public key
    long long int B_pub = modExp(g, y, p);  // Party B's public key

    // Key derivation
    long long int A_key = modExp(B_pub, x, p);  // Party A's shared key
    long long int B_key = modExp(A_pub, y, p);  // Party B's shared key

    // Output the generated keys
    std::cout << "Party A's shared key: " << A_key << std::endl;
    std::cout << "Party B's shared key: " << B_key << std::endl;

    return 0;
