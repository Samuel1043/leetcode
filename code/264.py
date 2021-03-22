class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i,j,k=0,0,0
        s=[1]
        for _ in range(n-1):
            val=min(s[i]*2,s[j]*3,s[k]*5)  
            if val==s[i]*2:
                i+=1
            if val==s[j]*3:
                j+=1
            if val==s[k]*5:
                k+=1
            s.append(val)
            # print(i,j,k,s,val)
        return s[-1]

if __name__ =='__main__':
    sol=Solution()
    print(sol.nthUglyNumber(30))