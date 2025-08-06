/*The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order. 
By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, 
determine whether it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.*/

#include <iostream>
#include<array>

// std::array<int, 4> numbers = {5, 2, 7, 8}; TESTING FIRST CASE

bool canReach24(std::array<int, 4> numbers) {
    return((numbers[0] * numbers[1] - numbers[2]) * numbers[3] == 24);
}

int main() {
    std::array<int, 4> userNumbers;

    for (int i = 0; i < 4; ++i){
        while (true){
            std::cout << "Enter four integers between 1 and 9: ";
            std::cin >> userNumbers[i];
            if (userNumbers[i] < 1 || userNumbers[i] > 9) {
                std::cout << "Invalid input. Please enter numbers between 1 and 9." << std::endl;
                continue; // Keep asking for input if invalid
            }
            break; // Exit loop if input is valid
        }
    }

    if (canReach24(userNumbers)) {
        std::cout << "Found a solution to reach 24!" << std::endl;
    } else {
        std::cout << "No solution found to reach 24." << std::endl;
    }
    return 0;
}