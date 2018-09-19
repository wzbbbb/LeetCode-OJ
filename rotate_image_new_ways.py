A=[[1,11,111,1111],[2,22,222,2222],[3,33,333,3333],[4,44,444,4444]]

def rotate(A):
  n = len(A)
  ''' create a new 2D list B, and assign value from A to B '''
  #B = [0,0,0,0]   # creating a new 2D list
  #for i in range(4):
  #  B[i] = [0] * 4
  B=A[:]
  for i in range(n):
    for j in range(n):
      B[i][j] = A[n-1-j][i]

  return B
print A
print rotate(A)

def rotate_in_place(A):
  """flip image diagonal (\) => i,j = j,i
   then flip  vertical from center """
  n = len(A)
  for i in range(n):
    for j in range(i+1,n):
      A[i][j], A[j][i] = A[j][i], A[i][j]

  for i in range(n):
    for j in range(n//2):
      A[i][j], A[i][n-j-1] = A[i][n-j-1], A[i][j] 

  return A
print rotate_in_place(A)
