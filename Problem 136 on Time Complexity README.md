136: Single Number
Link for question: https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

 My Solution:
To keep a linear runtime complexity, I have used Dictionary as the data structure as it uses hashing function to perform operations at O(1) runtime.
When we place it inside a loop, the runtime becomes O(N) as i am counting the occurences of every number in the list to store it in dictionary.

Time Complexity: O(N)
Approach: Hash Table / Brute Force Search
Alternative Approach: Bit Manipulation using XOR
