from typing import *
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        def backtrack(arr,lower,upper,total):
            if total==target:
                res.append(arr)
#           not in range of candidates[i]  
            prev=51
    
            for i in range(lower,upper):
                if prev==candidates[i]:
                    continue
                if total+candidates[i]>target:
                    return 
                backtrack(arr+[candidates[i]],i+1,upper,total+candidates[i])
                prev=candidates[i]
        res=[]
        backtrack([],0,len(candidates),0)
            
        return res
if __name__=='__main__':
    sol=Solution()
    print(sol.combinationSum2(candidates = [2,5,2,1,2], target = 5))
    print(sol.combinationSum2(candidates = [1,5,2,3], target = 5))
