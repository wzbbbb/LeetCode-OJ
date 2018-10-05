nums=[1,2,3,4,5,6,7]
k=3
#  Time Limit Exceeded  :(
def rotate( nums, k):
      """
      :type nums: List[int]
      :type k: int
      :rtype: void Do not return anything, modify nums in-place instead.
      """
      n = len(nums)
      k = k % n 
      for i in range(n-k, n):
          for j in range(n-k):
              nums[i-j], nums[i-j-1] = nums[i-j-1], nums[i-j]
      print nums

      return nums
print rotate( nums, k) 

# Submission Result: Accepted
''' array rotat : reverse the whole list, then reverse both 0 ->k and k -> n, separately
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
