board = [ ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
def isValidSudoku( board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for b in board:
        dic={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        for i in range(9):
            if b[i] == '.':
                continue
            if 0 < int(b[i]) < 10:
                dic[int(b[i])] +=1
            else:
                return False
        for d in dic.values():
            if d > 1:
                return False
    for i in range(9):
        dic={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        for b in board:
            if b[i] == '.':
                continue
            if 0 < int(b[i]) < 10:
                dic[int(b[i])] +=1
            else:
                return False
        for d in dic.values():
            if d > 1:
                return False
    for i in range(3):
        for j in range(3):
            dic={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
            for m in range(i*3, (i+1)*3):
                for n in range(j*3, (j+1)*3):
                    if board[m][n] == '.':
                        continue
                    if 0 < int(board[m][n]) < 10:
                        dic[int(board[m][n])] +=1
                    else:
                        return False
            for d in dic.values():
                if d > 1:
                    return False

    return True
print isValidSudoku( board)
