class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # in this problem we will calculate remainder at every index by summing numbers
        # and store in hashmap
        # if the remainder is repaeted then its like number is repaeated
        # so we will take diffrence it must be greater than 1 because in question they
        # mentioned must be atlesat 2 and also we inserted 0 it should not be counted
        m = {
            0: -1
        }
        sm = 0
        for i, n in enumerate(nums):
            sm += n
            r = sm % k
            if(r not in m):
                m[r] = i
            elif(i-m[r] > 1):
                return True
        return False
