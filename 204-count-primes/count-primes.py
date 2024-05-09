class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False] * (n + 1)
        count = 0

        for i in range(2, int(n ** 0.5) + 1):
            if not sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = True

        for i in range(2, n):
            if not sieve[i]:
                count += 1

        return count