A = [2,4,6,7,28, 0,0,0,0]
B = [2,5,7,9]

def merge(A,B):
  m = 5
  n = len(B)
  p = m -1        # comparing point in A
  q = m + n  -1   # inset point in end of A
  while p >= 0 and B:
    print "p, q", p, q
    if B[-1] >= A[p] : 
      A[q] = B.pop()
      q -=1
    else:
      A[q] = A[p]
      q -=1
      p -=1
  if B == []: return A
  else: 
    k = len(B)
    for i in range(k):
      A[i] = B[i]
    return A

print merge(A,B)

# Submission Result: Accepted
# faster, without list operations
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        ''' keep 3 pointers for nums1, nums2 and the insert location k
        '''
        i, j, k = n -1, m -1, m + n -1
        while j >= 0 and i >= 0:
            if nums2[i] > nums1[j]:
                nums1[k] = nums2[i]
                i -= 1
            else:
                nums1[k] = nums1[j]
                j -=1
            k -=1                
        while i >= 0:
            nums1[k] = nums2[i]
            i -=1
            k -=1
        while j >= 0:
            nums1[k] = nums1[j]
            j -=1
            k -=1
