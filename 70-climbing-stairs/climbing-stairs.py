class Solution:
    def climbStairs(self, n: int) -> int:
        x,y=1,1

        for i in range(n-1):
            temp = y
            y = x+y
            x = temp
        return y
