import sys
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j = len(num1)-1,len(num2)-1
        res = [];car = 0
        while( i >= 0  or  j >= 0):
            #if 123 and 2 then we make like 002 with below logic
            dig1 = int(num1[i]) if (i >= 0) else 0
            dig2 =  int(num2[j]) if( j >= 0) else 0

            tt =  dig1 + dig2 + car
            car = tt // 10
            # add the modulo for res it goes in reverse order
            res.append(str(tt%10))
            i -= 1
            j -= 1
        if car:
            res.append(str(car))
        # print(res)
        return "".join(res[::-1])

        
  #do this problem like we add 2 numbers with carry(its easy no more tense required)  done on own     