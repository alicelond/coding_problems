/*Given integers M and N, write a program that counts how many positive integer 
pairs (a, b) satisfy the following conditions:

a + b = M -> b = M - a
a XOR b = N*/

#include<iostream>

int main() {

    int M, N;
    int a, b;
    int count = 0;
    
    std::cout << "Enter M: ";
    std::cin >> M;  // Read both M and N from input
    std::cout << "Enter N: ";
    std::cin >> N;  // Read both M and N from input

    for(a = 1; a < M; a++){
        b = M - a;

        // Check if a XOR (^) b equals N
        // Converts the number to binary and performs XOR operation
        if(a ^ b == N){ 
            count++;
            std::cout << "Pair found: (" << a << ", " << b << ") - Count: " << count << "\n";
        }
    }
    return 0;
}