digits = '6504451329'
def letters(digits):
  pad = []
  pad.append('+')        #
  pad.append(' ')        # index 1
  pad.append('abc')
  pad.append('def')
  pad.append('ghi')
  pad.append('jkl')
  pad.append('mno')
  pad.append('pqrs')
  pad.append('tuv')
  pad.append('wxyz')
  n = len(digits)
  res, s = [''], ''
  for i in range(n):
    di = digits[i]
    tmp = []
    for t in res:
      for j in pad[int(di)]:
        s = t + j 
        tmp.append(s)
    res = tmp[:]
  return res
print letters(digits)



