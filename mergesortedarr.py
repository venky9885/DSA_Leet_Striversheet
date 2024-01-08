class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1.remove(0)
            nums1.append(nums2[i])
        nums1.sort()

        

# Runtime
# Details
# 38ms
# Beats 87.55%of users with Python3
# Memory
# Details
# 17.46MB
# Beats 6.70%of users with Python3