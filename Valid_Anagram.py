# Submission Result: Time Limit Exceeded  :(
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ''' anagram means chars rearrange within a word'''
        A = []
        for s1 in s:
            A.append(s1)
        for t1 in t:
            if t1 in A:
                A.remove(t1)
            else: 
                return False
        if A == []:
            return True
        else: 
            return False

# Submission Result: Time Limit Exceeded 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ''' anagram means chars rearrange within a word'''
        if len(t) != len(s):
            return False
        tmp2 = t
        for s1 in s:
            n = len(t)
            for i in range(n):
                if t[i] == s1:
                    tmp2 = t[:i] + t[i+1:]
            t = tmp2 
        if t == '':
            return True
        else:
            return False
#Submission Result: Accepted
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ''' anagram means chars rearrange within a word'''
        if len(t) != len(s):
            return False
        d1, d2 = {}, {}
        for s1 in s:
            if s1 not in d1.keys():
                d1[s1] = 1
            else:
                 d1[s1] +=1   
        for t1 in t:
            if t1 not in d2.keys():
                d2[t1] = 1
            else:    
                d2[t1] +=1
        return d1 == d2
