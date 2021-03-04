from typing import *
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # def backtrack(helper, lower, N):
        #     if len(tmp) == k:
        #         res.append(tmp[:])
        #         return
        #     for i in range(lower, N):
        #         if status[i]:
        #             status[i] = False
        #             tmp.append(helper[i])
        #             backtrack(helper, i, N)
        #             tmp.pop()
        #             status[i] = True
        # res = []
        # tmp = []
        # helper = [i+1 for i in range(n)]
        # status = [True for i in range(n)]
        # backtrack(helper, 0, n)

        # return res
        def backtrack(arr,lower,upper):
            if len(arr)==k:
                res.append(arr)
                return 
            for i in range(lower,upper):
                backtrack(arr+[i],i+1,upper)
            
        res=[]
        backtrack([],1,n+1)
        return res

if __name__ =='__main__':
    sol=Solution()
    print(sol.combine(1,1))