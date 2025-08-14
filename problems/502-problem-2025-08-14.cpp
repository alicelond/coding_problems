/*
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Example 2:
Input: n = 3
Output: 2
Example 3:
Input: n = 4
Output: 3

Constraints:
0 <= n <= 30
*/
#include <iostream>

int LoopFibonacci(){
    int previous = 0, current = 1;
    std::cout << "Fibonacci number 0 is: " << previous << std::endl;
    std::cout << "Fibonacci number 1 is: " << current << std::endl;

    for(int i = 2; i <= 30; i++){
        int fibonacci_number = previous + current;
        std::cout << "Fibonacci number " << i << " is: " << fibonacci_number << std::endl;
        previous = current;
        current = fibonacci_number;
    }
    return current;
}

int RecursionFibonacci(int previous, int current, int counter){
    if (counter <= 30){
        int fibonacci_number = current + previous;
        std::cout << "Fibonacci number " << counter << " is: " << fibonacci_number << std::endl;
        RecursionFibonacci(current, fibonacci_number, counter + 1);
    }
    return current;
}

int main(){
    std::cout << "Loop version:" << std::endl;
    LoopFibonacci();
    
    std::cout << "\nRecursive version:" << std::endl;
    RecursionFibonacci(0, 1, 2);  // Start with F(0)=0, F(1)=1, counter=2

    return 0;
}