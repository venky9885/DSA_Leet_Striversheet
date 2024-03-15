
# do this after house robber
# also watch https://www.youtube.com/watch?v=7FCemBxvGw0
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0

        for i in range(len(nums)):
            curEarn = nums[i]*count[nums[i]]
            # in question given nums[i] - 1 and every element equal to nums[i] + 1.
            # but you use  nums[i-1]+1 any how its equal
            # take care earn2 to use after 0 index because nums[i-1] goes out of index
            # here think [2,3,5,6] with 6 as current
            if(i > 0 and nums[i] == nums[i-1]+1):
                temp = earn2
                earn2 = max(curEarn+earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn+earn2
                earn1 = temp
        return max(earn1, earn2)
