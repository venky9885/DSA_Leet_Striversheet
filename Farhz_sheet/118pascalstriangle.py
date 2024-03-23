# https://leetcode.com/problems/pascals-triangle/

import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        full = [[1]]
        for i in range(1,numRows):
            temp = [1]
            for j in range(1,((i+1)//2)):
                temp.append(full[i-1][j-1]+full[i-1][j])
            if((i)%2 == 0 ):
                print(((i+1)//2),"555",full)
                ch = full[i-1][((i+1)//2)] +full[i-1][((i+1)//2)-1]
                temp.append(ch)
                temp.extend(temp[:-1][::-1])
                full.append(temp)
            else:
                temp.extend(temp[::-1])
                full.append(temp)
        print(full)
        # gr = [[1]]
        # for i in range(1,numRows):
        #     newlst  = []
        #     lp  = (i//2)+1
        #     ls1 = [1]
        #     ls2 = []
        #     for j in range(1,lp):
        #         if((i)%2 == 0 and  j==lp-1):
        #             # newlst.append(gr[i-1][lp-j-1]+gr[i-1][lp-j])
        #             print(ls2)
        #             ls2.append(gr[i-1][lp-j-1]+gr[i-1][lp-j])
        #             print(ls2)
        #             print("Continue",i,j,lp)
        #             continue
        #         ls1.append(gr[i-1][j-1]+gr[i-1][j])
        #         ls2.insert(0,gr[i-1][lp-j-1]+gr[i-1][lp-j])
        #         # newlst.append(gr[i-1][j-1]+gr[i-1][j])
        #         # newlst.append(gr[i-1][lp-j-1]+gr[i-1][lp-j])
        #     ls2.append(1)
        #     newlst.extend(ls1)
        #     newlst.extend(ls2)
        #     gr.append(newlst)
        # print(gr)
        return full