class Solution:
    # @return a string
  def intToRoman(self, num):
        res,n='',num
        th=n/1000
        r=n-th*1000
        h=r/100
        r=r - h*100
        t=r/10
        r = r- t * 10
        d = r
        if th > 0: res+='M' * th
        if h ==9 : res+='CM'
        elif h >= 5 and h !=9 : res+='D'+'C' * (h -5)
        elif h ==4 : res+='CD'
        else: res+='C' * h
        if t == 9: res+='XC'
        elif t>= 5 and t !=9 : res+='L' +'X' *(t-5)
        elif t ==4: res +='XL'
        else: res+='X' *t
        if d ==9 : res+= 'IX'
        elif d >= 5 and d !=9: res+= 'V' + 'I' * (d -5)
        elif d ==4:  res+='IV'
        else : res+='I' *d
        return res

        

