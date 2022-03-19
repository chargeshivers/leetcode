"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
"""
def largestRectangleArea(self, heights: List[int]) -> int:
    n = len(heights)

    @memoize
    def less_from_left(i):
        if i==0: return -1
        res = i-1 
        while res>=0 and heights[res] >= heights[i]:
            res = less_from_left(res)
        return res 

    @memoize
    def less_from_right(i):
        if i==n-1: return n
        res = i+1 
        while res < n and heights[res] >= heights[i]:
            res = less_from_right(res)
        return res 
      
    return max( ( less_from_right(i) - less_from_left(i) -1   )*heights[i] for i in range(n))
