nums= [0,0,1,1,1,2,2,3,3,4]
# Submission Result: Time limit exceed , bad 
def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0 : return 0
    dic = {}
    max1=max(nums)
    i = 1
    while i <n:
        if nums[i-1] == nums[i]:
            nums[i] = max1 +1
            nums.sort()
            nums.pop()
            n -=1
        else:
            i +=1                   
    return len(nums)
print  removeDuplicates(nums)
# Submission Result: Accepted 
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0 : return 0
        i = 1
        while i <n:
            if nums[i-1] == nums[i]:
                nums.remove(nums[i])
                n -= 1
            else:
                i += 1                   
        return len(nums)
