# Sieve of Eratosthenes
# O(sqrt(n) * loglogn) time | O(n) space
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [False, False] + [True] * (n-2) # 0 and 1 are not prime
        for p  in range(2, int(sqrt(n)) + 1): # O(sqrt(n)) time
            
            # idea: if a number is prime
            if primes[p]:
                # all of its multiples are not primes
                for multiple in range(p*p, n, p): # O(loglogn) time, proof: http://www.cs.umd.edu/~gasarch/BLOGPAPERS/sump.pdf
                    primes[multiple] = False
        
        return sum(primes)


# ------------------

# O(n^2) time | O(1) space
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        
        for i in range(2, n):
            isPrime = True
            for j in range(2, n):
                if i == j:
                    continue
                if i % j == 0:
                    isPrime = False
            if isPrime:
                res += 1
        
        return res