# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            for j in range(i+1,n):
                if(abs(nums[i]-nums[j]) == k and (nums[i],nums[j]) not in res):
                    res.add((nums[i],nums[j]))
        print(res)
        return len(res)
# the above solution will work search for real sutable with all hints given
# below bin search solution
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        # Base Case:
        if k < 0:
            return 0

        nums.sort()
        unique_pairs = 0
        ans = set()


        for ind in range(len(nums)):
            num2 = nums[ind] + k
            # binary Search:
            left = ind + 1
            right = len(nums) - 1

            while left <= right:

                mid = left + (right-left)//2
                if nums[mid] == num2:
                    unique_pairs += 1
                    ans.add((nums[ind], nums[ind]+k))
                    break
                elif nums[mid] > num2:
                    right = mid - 1
                else:
                    left = mid + 1

        return len(ans)             
                    

        