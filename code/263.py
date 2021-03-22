class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n==1:
            return True
        n=abs(n)
        while n>1:
            print(n)
            if n%5==0:
                n=n//5
            elif n%3==0:
                n=n//3
            elif n%2==0:
                n=n//2
            else:
                return False
        return True
if __name__ =='__main__':
    sol=Solution()
    print(sol.isUgly(-2147483648))