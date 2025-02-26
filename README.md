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

## 4.Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
### Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
### Example 2:
Input: strs = ["x"]
Output: [["x"]]
### Example 3:
Input: strs = [""]
Output: [[""]]
### Constraints:

    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.
### Time & Space Complexity: 
You should aim for a solution with O(m * n) time and O(m) space, where m is the number of strings and n is the length of the longest string. 

## 5.Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
### Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]
### Example 2:
Input: nums = [7,7], k = 1
Output: [7]
### Constraints:

    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.
### Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

The implementation of the solution uses Python's Counter class from the collections module to calculate the frequency of each element in the nums array. Counter is essentially a hash map or a dictionary that maps each element to its frequency.
Here's a step-by-step walkthrough of the implementation:
First, we use Counter(nums) to create a frequency map that holds the count of each number in the nums array.
Next, we initialize an empty min-heap hp as a list to store tuples of the form (frequency, num), where frequency is the frequency of the number num in the array.
We iterate over each item in the frequency map and add a tuple (freq, num) to the heap using the heappush function.
While we add elements to the heap, we maintain the size of the heap to not exceed k. If adding an element causes the heap size to become greater than k, we pop the smallest item from the heap using heappop. This is done to keep only the k most frequent elements in the heap.
After we finish processing all elements, the heap contains k tuples representing the k most frequent elements. The least frequent element is on the top of the min-heap, while the k-th most frequent element is the last one in the heap's binary tree representation.
Finally, we build the result list by extracting the num from each tuple (freq, num) in the heap using a list comprehension: [v[1] for v in hp].
Let's use a small example to illustrate the solution approach. Consider the array nums = [1,2,3,2,1,2] and k = 2. Our goal is to find the 2 most frequent elements in nums.
We first use Counter(nums) to create a frequency map. This gives us {1: 2, 2: 3, 3: 1} where the key is the number from nums and the value is its frequency.
We initialize an empty min-heap hp. It's going to store tuples like (frequency, num).
We iterate over the frequency map and add each num and its frequency to hp. For example, (2, 1) for the number 1 with a frequency of 2. We use heappush to add the tuples to hp, so after this step hp might have [(1, 3), (2, 1)].
The heap should not exceed the size k. In our case, k is 2, which means after we add the third element (3, 2), we need to pop the smallest frequency. So we end up with hp as [(2, 1), (3, 2)] after all the operations since (1, 3) would be the popped element because it had the lowest frequency.
The heap now contains the tuples for the 2 most frequent elements. The tuple with the smallest frequency is at the top, ensuring that less frequent elements have been popped off when the size limit was exceeded.
Finally, to build our result list, we extract the number from each tuple in the heap. Using list comprehension [v[1] for v in hp] we get [1, 2], which are the elements with the highest frequency. This is our final result and we can return it.
Following this approach, we implemented an efficient solution to the problem that avoids sorting the entire frequency map directly and instead maintains a heap of size k to track the k most frequent elements.
