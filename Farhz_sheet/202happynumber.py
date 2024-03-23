class Solution:
    def isHappy(self, n: int) -> bool:
        st = {}
        def r(nm):
            
            nonlocal st
            if(nm in st and st[nm] == 2):

                print(nm,st)
                return False
            if(nm == 1):
                return True
            sm = 0
            for i in str(nm):
                sm+=int(i)*int(i)
            if sm in st:
                st[sm] +=1
            else:
                st[sm] = 1
            return r(sm)
        return r(n)

    #very easy
