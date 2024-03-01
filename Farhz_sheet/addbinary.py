class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        car = 0
        i,j = len(a)-1,len(b)-1
        while(i >= 0 or j >= 0 or car):
            total =  car
            if(i >= 0):
                total+=int(a[i])
                i-=1
            if( j >= 0):
                total += int(b[j])
                j-=1
                #here %2 is because binary operation leaves remainder 0 or 1
            res.append(str(total%2))
            car = total//2
        print(res)
        return ''.join(res)[::-1]












#dont use below solution do binary addition
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        print()
        return str(bin(a+b)).replace("0b","")
