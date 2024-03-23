class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n= columnNumber
        res = ""
        while(n > 0):
            #Decrement the value of n by 1, to fit the number system starting with 0 instead of 1.
            n -= 1
            #here ord('A') gives number for A it is 68 ,then this helps to retrive char without makijng dict
            res = chr(n%26 + ord('A'))+res
            n = n//26
        return res
