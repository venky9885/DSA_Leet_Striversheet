class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        #here undertand main logic
        #take 9/3 => range(0,9-3+1,3) => 0, 3, 6, 9. =>length is 4
        result = len(range(0, dividend-divisor+1, divisor))
        if sign == -1:
            result = -result
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)
        return result
    #this below solution could not be used as  / operator shold not be used
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r = int(dividend/divisor)
        # print(2**31)
        if(r >= 2**31):
            return r-1
        elif( r <= -2**31):
            return r
        return int(dividend/divisor)