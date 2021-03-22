import math
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n<3:
            return 0
        
        # primes=[2]
        
        # for i in range(3,n):
        #     is_prime=True
        #     for prime in primes:
        #         if i%prime==0:
        #             is_prime=False
        #             break
        #     if is_prime:
        #         primes.append(i)
        # return len(primes)
        
        # approach 2 Sieve of Eratosthenes
        primes = n*[1]
        primes[0]=primes[1]=0
        for i in range(2,int(math.sqrt(n))+1):
            if primes[i]:
                for j in range(i*i,n,i):
                    primes[j]=0
        return sum(primes)
if __name__ =='__main__':
    sol=Solution()
    print(sol.countPrimes(10))

