# https://leetcode.com/problems/subsets/


res = []

# this might be different know the difference
def subsetmult(arr,ind,aux):
    # print(arr,ind,aux)
    if(ind ==  len(arr)):
        return
    for i in range(len(arr[ind:])):
        aux.append(arr[ind])
        if(aux not in res):
            res.append(aux.copy())
        
        subset(arr,ind+1,aux)
        
        aux.pop()
        if(aux not in res):
            res.append(aux.copy())
        subset(arr,ind+1,aux)


def subsets(arr,ind,hp,sol):
    if(len(arr) == ind):
        print(hp)
        sol.append(hp.copy())
        return
    hp.append(arr[ind])
    subsets(arr,ind+1,hp,sol)
    hp.pop()
    subsets(arr,ind+1,hp,sol)
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        hp = []
        subsets(nums,0,hp,sol)
        return sol
        #mult subsets
        # res.clear()
        # subset(nums,0,[])
        # return res


        
#!  Solution From chat gpt  with loop
# def subsets(arr, ind, hp, sol):
#     if len(arr) == ind:
#         print(hp)
#         sol.append(hp.copy())
#         return
  
#     for i in range(ind, len(arr)):
#         hp.append(arr[i])
#         subsets(arr, i + 1, hp, sol)
#         hp.pop()
# !without loop

# def subsets(arr,ind,hp,sol):
#     if(len(arr) == ind):
#         print(hp)
#         sol.append(hp.copy())
#         return
#     hp.append(arr[ind])
#     subsets(arr,ind+1,hp,sol)
#     hp.pop()
#     subsets(arr,ind+1,hp,sol)
    
    
# arr = [1, 2, 3]
# sol = []
# subsets(arr, 0, [], sol)
# print("Subsets using subsets with for loop:", sol)        