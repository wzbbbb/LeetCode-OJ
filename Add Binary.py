class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
  def addBinary(self, a, b):
    na=int(a,2)
    nb=int(b,2)
    s=na+nb
    return bin(na+nb)[2:]

        
      

