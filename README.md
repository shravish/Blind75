# Blind75

## 1.Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
### Example 1:
Input: nums = [1, 2, 3, 3]
Output: true
### Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
### Time & Space Complexity: 
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array. 

## 2.Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
### Example 1:
Input: s = "racecar", t = "carrace"
Output: true
### Example 2:
Input: s = "jar", t = "jam"
Output: false

## 3.Two Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.
### Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
### Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]
Explanation: nums[0] + nums[2] == 10, so we return [0, 2].
### Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]
Explanation: nums[0] + nums[1] == 10, so we return [0, 1].
### Constraints
    2 <= nums.length <= 1000
    -10,000,000 <= nums[i] <= 10,000,000
    -10,000,000 <= target <= 10,000,000
### Time & Space Complexity: 
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array. 
