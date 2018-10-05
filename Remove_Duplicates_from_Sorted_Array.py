nums= [0,0,1,1,1,2,2,3,3,4]
# Submission Result: Accepted 
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
