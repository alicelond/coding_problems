/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
*/
#include <vector>
#include <unordered_map>
#include <gtest/gtest.h>
#include <algorithm>

using namespace std;

vector<int> twoSumBruteForce(vector<int>& nums, int target){
    /*This function has time complexity of O(n^2), because of the nested for loops.*/
    vector<int> target_indices;

    for(int i = 0; i < nums.size(); i++){
        for(int j = i+1; j < nums.size(); j++){

            if(nums.at(i) + nums.at(j) == target){
                target_indices.push_back(i);
                target_indices.push_back(j);
                break;
            }
        }
    }    
    return target_indices;
}

vector<int> twoSumHashMap(vector<int>& nums, int target){
    /*This function has time complexity of O(n).*/
    vector<int> target_indices;

    unordered_map<int, int> hash_table;
    for (int i = 0; i < nums.size(); i++){
        int second_integer = target - nums.at(i);

        auto it = hash_table.find(second_integer);
        if(it != hash_table.end()){
            target_indices.push_back(i);
            target_indices.push_back(it->second);
            break;
        }else {
            hash_table[nums.at(i)] = i;
        }
    }
    return target_indices;
}

// Helper function to check if two vectors contain the same elements (order doesn't matter)
bool vectorsEqual(const vector<int>& a, const vector<int>& b) {
    if (a.size() != b.size()) return false;
    vector<int> sortedA = a;
    vector<int> sortedB = b;
    sort(sortedA.begin(), sortedA.end());
    sort(sortedB.begin(), sortedB.end());
    return sortedA == sortedB;
}

// Tests for BruteForce method
TEST(TwoSumBruteForceTest, Example1) {
    /*Setup*/
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> expected = {0, 1};
    /*Act*/
    vector<int> result = twoSumBruteForce(nums, target);
    /*Assert or expect*/
    EXPECT_TRUE(vectorsEqual(result, expected)) 
        << "Expected: [0, 1] or [1, 0], Got: [" 
        << result[0] << ", " << result[1] << "]";
}

TEST(TwoSumBruteForceTest, Example2) {
    /*Setup*/
    vector<int> nums = {3, 2, 4};
    int target = 6;
    vector<int> expected = {1, 2};
    /*Act*/
    vector<int> result = twoSumBruteForce(nums, target);
    /*Assert*/
    EXPECT_TRUE(vectorsEqual(result, expected)) 
        << "Expected: [1, 2] or [2, 1], Got: [" 
        << result[0] << ", " << result[1] << "]";
}

TEST(TwoSumBruteForceTest, Example3) {
    vector<int> nums = {3, 3};
    int target = 6;
    vector<int> expected = {0, 1};
    
    vector<int> result = twoSumBruteForce(nums, target);
    
    EXPECT_TRUE(vectorsEqual(result, expected)) 
        << "Expected: [0, 1] or [1, 0], Got: [" 
        << result[0] << ", " << result[1] << "]";
}

// Tests for HashMap method
TEST(TwoSumHashMapTest, Example1) {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> expected = {0, 1};
    
    vector<int> result = twoSumHashMap(nums, target);
    
    EXPECT_TRUE(vectorsEqual(result, expected)) 
        << "Expected: [0, 1] or [1, 0], Got: [" 
        << result[0] << ", " << result[1] << "]";
}

TEST(TwoSumHashMapTest, Example2) {
    vector<int> nums = {3, 2, 4};
    int target = 6;
    vector<int> expected = {1, 2};
    
    vector<int> result = twoSumHashMap(nums, target);
    
    EXPECT_TRUE(vectorsEqual(result, expected)) 
        << "Expected: [1, 2] or [2, 1], Got: [" 
        << result[0] << ", " << result[1] << "]";
}

TEST(TwoSumHashMapTest, Example3) {
    vector<int> nums = {3, 3};
    int target = 6;
    vector<int> expected = {0, 1};
    
    vector<int> result = twoSumHashMap(nums, target);
    
    EXPECT_TRUE(vectorsEqual(result, expected)) 
        << "Expected: [0, 1] or [1, 0], Got: [" 
        << result[0] << ", " << result[1] << "]";
}

// Additional edge case tests for both methods
TEST(TwoSumEdgeCases, LargeNumbers) {
    vector<int> nums = {-1000000000, 1000000000};
    int target = 0;
    vector<int> expected = {0, 1};
    
    vector<int> result1 = twoSumBruteForce(nums, target);
    vector<int> result2 = twoSumHashMap(nums, target);
    
    EXPECT_TRUE(vectorsEqual(result1, expected));
    EXPECT_TRUE(vectorsEqual(result2, expected));
}

TEST(TwoSumEdgeCases, NegativeNumbers) {
    vector<int> nums = {-3, 4, 3, 90};
    int target = 0;
    vector<int> expected = {0, 2}; // -3 + 3 = 0
    
    vector<int> result1 = twoSumBruteForce(nums, target);
    vector<int> result2 = twoSumHashMap(nums, target);
    
    EXPECT_TRUE(vectorsEqual(result1, expected));
    EXPECT_TRUE(vectorsEqual(result2, expected));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}




