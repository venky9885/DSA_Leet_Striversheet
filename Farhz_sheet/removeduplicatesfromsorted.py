# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tp = sorted(set(nums))
        ct = len(nums)-len(tp)
        tp.extend(("_" for i in range(ct) ))
        nums.clear()
        tp = list(tp)
        # tp.sort()
        nums.extend( tp)
        return ct

        