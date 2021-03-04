from typing import *
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    # !constrained Only numbers 1 through 9 are used
        limit=10
        def backtrack(arr,depth,lower,upper,total):
            if depth==k+1:
                if total==n:
                    res.append(arr)
                return
            for i in range(lower,upper):
                if total+i>n:
                    continue
                backtrack(arr+[i],depth+1,i+1,min(limit,upper+1),total+i)
        res=[]

        backtrack([],1,1,min(n-k+1,limit),0)
        return res
if __name__ =='__main__':
    sol=Solution()
    print(sol.combinationSum3(k = 3, n = 7))
    print(sol.combinationSum3(k = 3, n = 9))
    print(sol.combinationSum3(k = 3, n = 2))
    print(sol.combinationSum3(k = 4, n = 1))
    print(sol.combinationSum3(k = 8, n = 36))
