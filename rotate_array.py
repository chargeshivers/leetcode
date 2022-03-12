"""
https://leetcode.com/problems/rotate-array/
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
def rotate(self, nums: List[int], k: int) -> None:
    def reverse(i,j):
        """ 
        reverses the i to j range of nums
        """ 
        start, end = i,j 
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    n = len(nums)
    k %= n
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
