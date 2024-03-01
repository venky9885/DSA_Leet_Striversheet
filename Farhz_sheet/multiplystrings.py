#this below code is not perfect because they said to not use int to convert directly ,so check new solution
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        revnm2 = num2[::-1]
        re = 0
        for i in range(len( num2)):
            re+=int(str(int(num1)*int(revnm2[i]))+ "0"*i)
        print(re)
        return str(re)
