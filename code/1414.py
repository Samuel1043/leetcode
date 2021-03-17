class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
    
        fibarr=[1]
        while fibarr[-1]<k:
            if len(fibarr)<2:
                fibarr.append(1)
            else:
                fibarr.append(sum(fibarr[-2:]))

        N=len(fibarr)
        ans=0
        for i in range(N-1,-1,-1):
            if k==0:break
            if k>=fibarr[i]:
                k-=fibarr[i]
                ans+=1
        return ans

if __name__=='__main__':
    sol=Solution()
    print(sol.findMinFibonacciNumbers(10))
    print(sol.findMinFibonacciNumbers(1))
    print(sol.findMinFibonacciNumbers(19))
    print(sol.findMinFibonacciNumbers(7))



