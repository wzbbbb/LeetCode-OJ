A=[100, 2, 7, 11, 15, 10]
t=111
def twosum(A,t):
  n = len(A)
  dic=dict()
  for i in range(n): 
    dic[A[i]] = i
  A.sort()
  for i in range(n - 1):
    for j in range(i + 1, n):
      if A[i] + A[j] == t:
        ind1 = min(dic[A[i]], dic[A[j]])
        ind2 = max(dic[A[i]], dic[A[j]])
        return   ind1 + 1, ind2 + 1
      elif A[i] + A[j] > t:
        break

print twosum(A,t)
#  Submission Result: Accepted  57%
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        A = sorted(nums)
        n = len(A)
        for i in range(n):
            for j in range(i+1, n):
                if A[i] + A[j] > target:
                    break
                elif A[i] + A[j] == target:
                    p = nums.index(A[i])                        # when you have input like [3,3]
                    q = n - 1 - nums[::-1].index(A[j])
                    return [p , q]

# Submission Result: Accepted , slower
# not sorted
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            if (target - nums[i]) in nums[i+1:]:
                return [i, n - 1 - nums[::-1].index(target - nums[i])]

# Submission Result: Accepted , using dict is much slower
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        A = sorted(nums)
        n = len(A)
        d = {}
        for i in range(n):
            if nums[i] not in d.keys():
                d[nums[i]] = [i]
            else:
                d[nums[i]] += [i]
        for i in range(n):
            for j in range(i+1, n):
                if A[i] + A[j] > target:
                    break
                elif A[i] + A[j] == target:
                    return [d[A[i]][0], d[A[j]][-1]]
