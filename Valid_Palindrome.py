S = 'A man, a plan, a canal: Panama '
#S = "race a car"
#S = ''
def validate(S):
  res = ''
  for s in S:
    if s.isalpha():
      res += s.lower()
  return res == res[::-1]

print  validate(S)



