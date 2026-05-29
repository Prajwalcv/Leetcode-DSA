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
Space Complexity (Current Approach): O(N) - Dictionary stores up to N/2 unique elements
Space Complexity (Suggested/Optimal Approach): O(1) - Using Bit Manipulation with XOR operator

Approach: Hash Table / Brute Force Search
Alternative Approach: Bit Manipulation using XOR (Optimal - satisfies O(1) space constraint)

Note: The problem constraint requires constant extra space O(1). The optimal solution uses XOR bit manipulation where a^a=0 and a^0=a, causing all paired numbers to cancel out and leaving only the single number.
