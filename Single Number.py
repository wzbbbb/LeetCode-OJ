class Solution:
    # @param A, a list of integer
    # @return an integer
  def singleNumber(self, A):
	x=0 
	for a in A:
		x^=a
	return x

