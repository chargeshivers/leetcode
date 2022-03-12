"""
https://leetcode.com/problems/subsets/
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
def subsets(nums: List[int]) -> List[List[int]]:
    def f(i):
        if i<0:
            return [[]]
        S = f(i-1)
        return S + [ s+[nums[i]] for s in S ]
    return f(len(nums)-1)
