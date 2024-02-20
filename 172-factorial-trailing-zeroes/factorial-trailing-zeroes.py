class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            if i % 5 == 0:
                while True:
                    i = i / 5
                    if i % 5 == 0: count +=1
                    else: break
                count+=1
        return count