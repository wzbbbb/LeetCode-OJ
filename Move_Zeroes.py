# Submission Result: Accepted
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p, q = 0, 0 # p non-zero, q : zero
        n = len(nums)
        while p < n and q < n:
            while p < n: 
                if nums[p] == 0:
                    p += 1
                else: 
                    break
            while q < n:
                if nums[q] != 0:
                    q +=1
                else:
                    break
            if p >= n or q >=n: 
                break
            if p > q:
                nums[p], nums[q] = nums[q], nums[p]
                q += 1
                p += 1
            else:
                p +=1

# Submission Result: Accepted
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for n in nums:
            if n == 0:
                nums.remove(0)
                nums.append(0)
   
