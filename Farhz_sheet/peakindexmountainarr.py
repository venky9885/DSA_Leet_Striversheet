class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0,len(arr)-1
        # it is like doing binary search without target
        while(l <= r):
            m = (l+r)//2
            #think arr[m-1] is 4 arr[m] is 5 and arr[m+1] is 6
            if(arr[m-1] <= arr[m] and arr[m]  >= arr[m+1] ):
                return m
            #ex:  0,10,5,2 -> (10 > 5) then r = 10
            elif(arr[m-1] > arr[m]):
                r = m
            else:
                l = m

        