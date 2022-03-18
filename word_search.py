"""
https://leetcode.com/problems/word-search/
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""
def exist(board: List[List[str]], word: str) -> bool:
    m = len(board)
    n = len(board[0])
    if m*n <len(word) or  set(word).difference( set(  [  board[i][j]  for i in range(m) for j in range(n)  ]  )     ):  
        return False
        
    def is_valid(pos):
        i,j=pos
        return (i in range(m)) and (j in range(n))

    def neighbors(pos):
        i,j=pos
        return [ (i-1,j) , (i+1,j), (i,j-1), (i,j+1) ]
    
    def startFrom(pos,w):
        i,j=pos
        if w=='':
            return True
        if (not is_valid(pos)) or (w[0] != board[i][j]):
            return False
        else:
            board[i][j] = '#' 
            res = any(startFrom(v,w[1:] ) for v in neighbors(pos))
            board[i][j] = w[0]
            return res 
    
    return any(startFrom(  (i,j), word) for i in range(m) for j in range(n) )
