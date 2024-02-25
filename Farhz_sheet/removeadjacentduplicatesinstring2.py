class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [(s[0],1)]
        for i in s[1:]:
            if(stk and stk[-1][0] == i):
                if(stk[-1][1]+1 == k):
                    stk.pop()
                else:
                    stk[-1] = (i,stk[-1][1]+1)
            else:
                stk.append((i,1))
        # print(stk)
        re = ""
        for i in stk:
            re+=i[0]*i[1]
        return re
# remeber do it on way
#     Input: s = "deeedbbcccbdaa", k = 3
    #! cleanly observe it is doing on way there is no big logic
    # deeedbbcccbdaa
    # ddbbcccbdaa
    # ddbbbdaa
    # dddaa
    # aa
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"