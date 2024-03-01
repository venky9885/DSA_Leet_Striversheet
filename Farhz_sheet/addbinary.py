












#dont use below solution do binary addition
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        print()
        return str(bin(a+b)).replace("0b","")
