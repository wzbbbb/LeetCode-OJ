#Submission Result: Accepted 42%
class Solution(object):
  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    r1, r2 = 0, 0
    for num in nums:
      r1 += num
    n = len(nums)  
    for i in range(n + 1):
      r2 += i
    return r2 - r1
#Submission Result: Accepted 87%
class Solution(object):
  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    n = len(nums)  
    for i in range(n):
      res += i - nums[i]
    return res + n 
#Submission Result: Accepted , could be faster 
class Solution(object):
  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums) + 1
    return sum(range(n)) - sum(nums)
