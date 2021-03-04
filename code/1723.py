from typing import *
inf=float('inf')
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        N=len(jobs)

        def backtrack(lower,time):
            minval=inf
            upper=min(lower+k,N)
            for i in range(1,upper):
                print(lower,i,jobs[lower:lower+i],jobs[lower:])
                if lower+i==N-1:
                    return time+max(jobs[lower:])
                minval=min(backtrack(lower+i,time+max(jobs[lower:lower+i])),minval)
            return minval
        return backtrack(0,0)


if __name__ == "__main__":
    sol=Solution()
    print(sol.minimumTimeRequired(jobs = [3,2,3], k = 3))
    print(sol.minimumTimeRequired(jobs = [1,2,4,7,8], k = 2))