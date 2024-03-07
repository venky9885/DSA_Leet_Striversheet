#so simple and done on own
#for Ex : first take numRows as 4
# it will go 0,1,2,3
# then decrease backward 2,1
# in between ifv flag is true increment else decrement if reached end then set index to total len - 2 (si = numRows-2) or at starting si = 1

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows > 1): 
            l = [[] for _ in range(numRows)]
            flag = True
            si = 0
            for c in s:
                print(si,c)
                l[si].append(c)

                if(flag):
                    if(si == numRows-1):
                        # si = 0
                        flag = False
                        si = numRows-2
                    else:
                        si+=1

                else:
                    
                    if(si == 0):
                        flag = True
                        si = 1
                    else:
                        si-=1
            row = []
            for i in l:
                row.append(''.join(i))
            return ''.join(row)
        else:
            return s
