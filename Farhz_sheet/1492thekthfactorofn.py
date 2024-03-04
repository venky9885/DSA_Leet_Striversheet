#dead easy

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ct = 0
        i = 1
        while(i <= n):
            if(n%i == 0):
                print(n,i)
                ct+=1
            if(ct == k):
                return i
            i+=1
        return -1
        