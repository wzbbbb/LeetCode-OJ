class Solution:
    # @param A, a list of integer
    # @return an integer
  def singleNumber(self, A):
	x,y,z=0,0,0 # x,y,z for number shows are 1,2,3 times
	for a in A:
		y=y|x & a # if a shows twice, y include a, x & a includ a, assign to y
		x^=a      # for first time, x includ a
		z=x&y     # if x and y both has a, it shows 3 times
		x &=~z  # complement, 0->1; 1->0, if z has a, remove it from x and y
		y &=~z  # z the numbers that show up 3 times
	return x

