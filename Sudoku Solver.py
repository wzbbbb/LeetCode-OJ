class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
  def chk(self,board,i,j, num):
    b,sz=board,9
    if str(num) in b[i]: return False
    for k in range(sz): 
      if str(num) == b[k][j]: return False
    if i in range(0,3): p=range(0,3) 
    if i in range(3,6): p=range(3,6) 
    if i in range(6,9): p=range(6,9) 
    if j in range(0,3): q=range(0,3) 
    if j in range(3,6): q=range(3,6) 
    if j in range(6,9): q=range(6,9) 
    for pi in p :
      for qi in q:
        if str(num) == b[pi][qi] : return False
    return True
  def fillin(self, board,finished=False):
    sz=9
    empty=False
    for pi in range(sz): # find the next spot to fill
      if empty: break
      for qi in range(sz):
        if board[pi][qi] == '.':
          empty=True
          i=pi; j=qi
          break
    if empty ==False: 
      return board,True
    else:
      for k in range(1,10):
        if self.chk(board,i,j,k) : 
          st=board[i][:j] + [str(k)] +board[i][j+1:]
          board[i]=st
          board,finished=self.fillin( board, finished)
          if finished==False: 
            st=board[i][:j] + ['.'] +board[i][j+1:]
            board[i]=st
    return board, finished
  def solveSudoku(self, board,finished=False):
    board=self.fillin(board)

