A = [ 2,  3,  4,  2,  6,  2,  5,  1 ]
w = 3
''' create another pipe, when sliding window move, push in only the current max, and pop out the first 
    This is a naive implementation though 
''' 

def max_in_win(A,w):
  res = []
  pipe = [] 
  for a in A:
    pipe.append(a)
    if len(pipe) == w:
      res.append(max(pipe))
      pipe.reverse()
      pipe.pop()
      pipe.reverse()
  return res 
print max_in_win(A,w)



