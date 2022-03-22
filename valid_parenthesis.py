"""
https://leetcode.com/problems/longest-valid-parentheses/
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
"""

def longestValidParentheses(s: str) -> int:
    @cache
    def f(i):#longest ending at index i
        if i <= 0 or s[i] == '(': return 0
        if s[i-1] == '(': return f(i-2) + 2 
        elif i-1-f(i-1) >=0 and s[i-1-f(i-1)] == '(': return f(i-1) + f( i-1-f(i-1) -1 ) + 2 
        else: return 0

    return max((f(i) for i in range(len(s))), default =0) 
