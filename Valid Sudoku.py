class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
  def isValidSudoku(self, board):
    m=[set() for i in range(9)]
    n=[set() for j in range(9)]
    s=[set() for k in range(9)]
    for i in range(9):
      for j in range(9):
        if board[i][j] != '.':
          #print(board[i][j],i,j)
          if board[i][j] not in m[i]:
            m[i].add(board[i][j])
          else: return False
          if board[i][j] not in n[j]:
            n[j].add(board[i][j])
          else: return False
          if i in range(0,3) and j in range(0,3) :
            if board[i][j] not in s[0]:
              s[0].add(board[i][j]) 
            else: return False
          if i in range(0,3) and j in range(3,6): 
            if board[i][j] not in s[1]:
              s[1].add(board[i][j])
            else: return False
          if i in range(0,3) and j in range(6,9): 
            if board[i][j] not in s[2]:
              s[2].add(board[i][j]) 
            else: return False
          if i in range(3,6) and j in range(0,3) :
            if board[i][j] not in s[3]:
              s[3].add(board[i][j]) 
            else: return False
          if i in range(3,6) and j in range(3,6): 
            if board[i][j] not in s[4]:
              s[4].add(board[i][j])
            else: return False
          if i in range(3,6) and j in range(6,9): 
            if board[i][j] not in s[5]:
              s[5].add(board[i][j]) 
            else: return False
          if i in range(6,9) and j in range(0,3) :
            if board[i][j] not in s[6]:
              s[6].add(board[i][j]) 
            else: return False
          if i in range(6,9) and j in range(3,6): 
            if board[i][j] not in s[7]:
              s[7].add(board[i][j])
            else: return False
          if i in range(6,9) and j in range(6,9): 
            if board[i][j] not in s[8]:
              s[8].add(board[i][j]) 
            else: return False
    return True
 

