#A = [-2,1,1,-3,4,-1,2,1,-5,4]
A = [-2,-11,-1,-3,-4,-1,-2,-1,-5,-4]

def max_subarray(A):
  max1= None
  sum1 = None
  for a in A:
    if sum1 == None or (sum1 < 0 and sum1 < a):
      sum1 = a
    else: 
      sum1 += a
    if max1 == None or sum1 > max1:
      max1 = sum1
  return max1
  
print max_subarray(A)



def max_subarray(A):
  max1 = None
  sum1 = None
  for a in A:
    if sum1 == None:
      sum1 = a
    elif sum1 > 0:
      sum1 += a
    elif sum1 < 0 and sum1 < a:
      sum1 = a
    else:
      sum1 = None
    if max1 == None:
      max1 = sum1
    elif max1 < sum1:
      max1 = sum1
  return max1
print max_subarray(A)
