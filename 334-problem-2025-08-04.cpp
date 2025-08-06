/*The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order. 
By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, 
determine whether it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.*/

#include <iostream>
#include<array>

std::array<int, 4> numbers = {5, 2, 7, 8};

bool canReach24(std::array<int, 4> numbers) {
    if((numbers[0] * numbers[1] - numbers[2]) * numbers[3] == 24)
        return true;
    else
        return false; 
}

int main() {
    if (canReach24(numbers)) {
        std::cout << "Found a solution to reach 24!" << std::endl;
    } else {
        std::cout << "No solution found to reach 24." << std::endl;
    }
    return 0;
}