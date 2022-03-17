"""
https://leetcode.com/problems/path-sum-iii/
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    if not root: return 0

    def ps_with(r, ts):
        if not r: return 0
        return 1*(r.val==ts) + ps_with(r.left, ts-r.val)  + ps_with(r.right, ts-r.val)
            
    return ps_with(root, targetSum ) + pathSum(root.left, targetSum ) + pathSum(root.right, targetSum )
