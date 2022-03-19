"""
https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""
from utils import memoize
def canPartition(nums: List[int]) -> bool:
    if sum(nums)%2 !=0:
        return False
    @memoize
    def f(i,t):
        if t<0: return False
        if i<0: return t==0
        return f(i-1,t-nums[i]) or f(i-1,t)
    return f(len(nums)-1, sum(nums)//2)
