people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#people =  [[8,2],[4,2],[4,5],[2,0],[7,2],[1,4],[9,1],[3,1],[9,0],[1,0]]
def reconstructQueue(people):
  ''' sort by (x[1],x[0]), then the first item is good for sure
      then check and move item one by one based on x[1]'''
  # This one exceed time limit :(
  A = sorted(people, key=lambda x:(x[1],x[0]))
  n = len(A)
  i = 1
  while i < n:
    moving = True
    while moving:
      count = 0
      for j in range(i):
        if A[j][0] >= A[i][0]:
          count +=1
      if count > A[i][1] :
        A[i], A[i-1] = A[i-1], A[i]
        i -= 1
      elif count == A[i][1] :
        moving = False
        i +=1
  return A
#print reconstructQueue(people)

''' Leetcode solution
Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
E.g.
input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
subarray after step 1: [[7,0], [7,1]]
subarray after step 2: [[7,0], [6,1], [7,1]]
'''
# Submission Result: Accepted
def requeue(people):
  ''' So the idea is that sort by hight 
      Then find all people with the same hight
      then insert them based on its existing rank value
      lower ranked people insert first, for example, [5,0] before [5,2]
  ''' 
  A = sorted(people, key = lambda x:(x[0],x[1]))
  n = len(A)
  B = []*n
  C = []     #all, currently, tallest ones taken from A
  while A:
    C.append(A.pop())
    while A:                    # filling C with the same hight people
      if A[-1][0] == C[0][0]:
        C.append(A.pop())
      else: 
        break
    print '==',C
    C.sort(key = lambda x:x[1], reverse=True)
    while C:
      i = C[-1][1]
      B.insert(i,C.pop() )
  return B
print requeue(people)
