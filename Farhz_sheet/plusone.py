# https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = ''
        for i in digits:
            p+=str(i)
            
        # print(list(   str( int("".join(digits))+1  )  ))
        return list( str(int(p)+1) )
        