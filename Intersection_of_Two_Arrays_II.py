# Submission Result: Accepted
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        running = True
        while running:
            running = False
            tmp1 = nums1[::]
            tmp2 = nums2[::]
            for n in tmp1:
                if n in tmp2:
                    nums1.remove(n)
                    nums2.remove(n)
                    res.append(n)
                    running = True
                    break
        return res 
