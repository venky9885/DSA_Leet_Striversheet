# https://leetcode.com/problems/invalid-transactions/

def transList(tx):
    return tx.split(",")
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invt = []
        invt.clear()
        for i in transactions:
            if(int(i.split(",")[2]) > 1000):
                invt.append(i)
                continue
            # else:
            sp = i.split(",")
            for j in transactions:
                sp2 = j.split(",")
                if( abs(int(sp[1])-int(sp2[1])) <= 60 and sp[0] == sp2[0] and sp[3] != sp2[3] ):
                    invt.append(i)
                    break
        # print(invt)
        return invt


#this is correct solution with 2 loops O(n^2) as per hints