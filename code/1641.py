import math
class Solution:

    # bottom up
    # def countVowelStrings(self, n):

    #     dp[n][k] when k=1 consider u k=2 consider o,u k=3 consider i,o,u
    #     k=4 consider e,i,o,u k=5 consider a,e,i,o,u   n=number of char
    #     ex: dp[2][2]=dp[2][1]+dp[1][2]=1+2=3 consist of 'o'+'o' or 'u'(dp[1][2]) ,uu(dp[2][1])
    #     dp[2][3]=dp[2][2]+dp[1][3]=3+3 is 6 consist of ii,io,iu,oo,ou,uu

    #     dp=[[0,1,1,1,1,1],[0,1,2,3,4,5]]
    #     if n==1:
    #         return dp[-1][-1]
    #     for i in range(n-1):
    #         for j in range(1,6):
    #             dp[0][j]=dp[0][j-1]+dp[1][j]
    #         tmp=dp[0]
    #         dp[0]=dp[1]
    #         dp[1]=tmp
    #     return dp[-1][-1]


    # top down
    # n=3 start from (n,k) 3,5 = (2,1)+(2,2)+(2,3)+(2,4)+(2,5)
    # (2,2)=(1,1)+(1,2)  (2,3)=(1,1)+(1,2)+(1,3) .....
    # (2,1)=1 uu (2,2)=(1,1) u +(1,2) o,u = ou
    def countVowelStrings(self, n):
            seen = {}
            def rec(n,k):
                if n==1 or k==1:
                    return k
                if (n,k) in seen:
                    return seen[(n,k)]
                total=0
                for i in range(1,k+1):
                    total+= (n-1,i)
                seen[(n,k)]=total
                return total
            return rec(n,5)
    def countVowelStrings(self, n):
        '''
        convert problem into putting stick between char,
        consider the stick position as where the specific char
        should change,ex: aaeeio ⇒ 2a4e5i6o number represent idx,
        if len_char=n the first stick have n+1 position to put,
        second n+2..., and last char position don't need to be specify
        it is always at the end, and also not all the positon can be
        chosen it's combination not permution,so it will be divide by 4!,
        sol: (n+1)*(n+2)*(n+3)*(n+4)/4! for 5 unique char.
        '''
        # same solution but not same intuition, since comb represent n! /(k! *(n-k)!
        return math.comb(n+4,4)



if __name__ =='__main__':
    sol=Solution()
    print(sol.countVowelStrings(4))