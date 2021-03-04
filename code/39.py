from typing import *
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(arr,lower,upper,total):    
            if total>target:
                return 
            elif total==target:
                res.append(arr)
            for i in range(lower,upper):
                backtrack(arr+[candidates[i]],i,upper,total+candidates[i])
        res=[]
        backtrack([],0,len(candidates),0)
        return res

if __name__ =='__main__':
    sol=Solution()
    print(sol.combinationSum(candidates = [2,2,3,6,7], target = 7))