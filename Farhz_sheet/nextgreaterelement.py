class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def f(stk,m):
            for i in stk:
                    if(i > m):
                        return i
            return -1
        mem = {}
        ln = len(nums2)
        for i in range(ln):
            if(nums2[i] in nums1):
                stk = nums2[i+1:]
                
                mem[nums2[i]] = f(stk,nums2[i])
        ls = []
        print(mem)
        for i in nums1:
            ls.append(mem[i])
        return ls