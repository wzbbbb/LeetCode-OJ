''' adding up all numbers in binary, digit by digit
    then mod 3 by each digit,
    then combine them togeter to get the uniq number
'''
A = [3, 5, 8, 9, 1, 3, 7, 2, 5, 8, 1, 9, 2, 5, 3, 9, 1, 8 ,2 ]
def uniq_num(A):
  n = len(bin(max(A))) - 2
  res = [0] * n
  num = ''
  for a in A:
    b = bin(a)[2:]
    m = len(b)
    for i in range(m):
      res[i] += int(b[::-1][i])
  for i in range(n):
    res[i] =  res[i] % 3
  for r in res:
    num += str(r)
  return int(num[::-1], 2)

print uniq_num(A)
