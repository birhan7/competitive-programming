class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        i = 2
        while i < n:
            if prime[i]:
                j = i * i
                while j < n:
                    prime[j] = 0
                    j += i
            i += 1
        for i in range(1, n):
            prime[i] += prime[i - 1]
        return prime[n - 1]

        
        