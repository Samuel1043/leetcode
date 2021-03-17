from typing import *
inf=float('inf')
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
            '''
            similar to 698,473
            dfs solution
            '''
            N=len(jobs)
            if k>=N:
                return max(jobs)
            # assign to workers
            assign=[0]*k

            self.res=inf
            # assign to all the worker, without assign to same worker
            self.depth=-1

            def dfs(index):
                self.depth+=1
                if index==N:
                    self.res=min(self.res,max(assign))
                    return 
                # speed up if seen before dont calculate again
                seen=set()
                # speed up assign to different workers 
                for i in range(self.depth,self.depth+k):
                    i=i%k
                    if assign[i] in seen: continue
                    if assign[i]+jobs[index]>=self.res: continue
                    seen.add(assign[i])
                    assign[i]+=jobs[index]
                    dfs(index+1)
                    assign[i]-=jobs[index]
            dfs(0)
            return self.res

    def minimumTimeRequired_BS(self, jobs: List[int], k: int) -> int:
        '''
        DFS+BS(binary search)
        defined workers first and check with jobs assign
        '''
        jobs.sort(reverse = True)
        N=len(jobs)
        
        # to calculate current assignment is upper(False) or lower(True) compare to jobs
        def dfs(curr):
            if curr == N:
                return True
            for i in range(k):
                if workers[i]>=jobs[curr]: 
                    workers[i] -= jobs[curr]
                    if dfs(curr+1):
                        return True
                    workers[i] += jobs[curr]
                if workers[i]==x: break
            return False

#        BS initialize upper and lower of the solution
        left,right=max(jobs),sum(jobs)
        while right>left:
            x=(left+right)//2
            workers=[x]*k

            if dfs(0):
                right=x
            else:
                left=x+1
        return left
if __name__ == "__main__":
    sol=Solution()
    print(sol.minimumTimeRequired(jobs = [3,2,3,4], k = 3))
    print(sol.minimumTimeRequired(jobs = [1,2,4,7,8], k = 2))
    print(sol.minimumTimeRequired(jobs = [2,3,4],k=2))