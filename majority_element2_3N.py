class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        st = set()
        if(len(nums)==1):
            return [nums[0]]
        ln = len(nums)

        i = 0
        j = ln-1


        while(i < j):
            if(nums.count(nums[i]) > ln/3):
                
                st.add( nums[i])
            if(nums.count(nums[j]) > ln/3):
                st.add( nums[j])
            i+=1
            j-=1
        return list(st)
        
        


# 87
# ms
# Beats
# 99.50%
# of users with Python3
# Memory
# 18.60
# MB
# Beats
# 32.30%
# of users with Python3