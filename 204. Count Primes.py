class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2 :
            return 0
        prime = [1] * (n)
        prime[0] = 0
        prime[1] = 0
        
        for i in range(2,n):
            if prime[i]:
                prime[i+i:n:i] = [0] * len(prime[i+i:n:i])
        return sum(prime)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2 :
            return 0
        prime = [0] * (n+1)
        
        for i in range(2,n):
            if prime[i] == 0 :
                for j in range(i,n,i):
                    prime[j] += 1
        cnt = 0
        for i in prime:
            if i == 1 :
                cnt +=1
        return cnt
        