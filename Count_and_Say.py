n = 8 
def say(n):
  ''' A is the list of the sequence
      B is a break of A[i] with repeating chars '''
  A, i = ['1', '11'], 1
  while i < n:
    ss = ''
    m = len(A[i])
    B = []
    B.append(A[i][0])
    for j in range(1, m):
      if A[i][j] == A[i][j-1]:
        B[-1] += A[i][j] 
      else:
        B.append(A[i][j] )
    for b in B:
      ss +=str(len(b)) + b[-1]
    A.append(ss)
    #print A
    i +=1
  return A
print say(n)

