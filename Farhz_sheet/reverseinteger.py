class Solution:
    def reverse(self, x: int) -> int:
        if(  x == 0):
            return x
        rem = []
        t =  abs(x)
        while(t):
            rem.append(str(t%10))
            t=t//10
        print(rem)
        reversed_x = int("".join(rem)) if  x < 0 else -1 * int("".join(rem))
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        if(  x < 0):
            return -1 * int("".join(rem))
        
        return int("".join(rem))
        