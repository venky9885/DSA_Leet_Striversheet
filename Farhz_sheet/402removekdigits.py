# https://www.youtube.com/watch?v=cFabMOnJaq0


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for c in num:
            # its simple if in stack last number greater than current number pop it else add it
            while k > 0 and stk and stk[-1] > c:
                k -= 1
                stk.pop()
            stk.append(c)
        # print(stk)
        # stk =stk[:5-2]= stk[:3] if it directly out if loop then we will rmove from last end
        stk = stk[:len(stk)-k]
        # lstrip to remove leading zeroes
        res = "".join(stk).lstrip('0')

        return res if (res) else "0"
