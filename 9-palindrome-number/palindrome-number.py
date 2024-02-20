class Solution:
    def isPalindrome(self, x: int) -> bool:
        # y = str(x)
        # return y == y[::-1]

        # follow up without converting
        if x < 0: return False
        div = 1
        while x >= 10 * div:
            div*=10
        
        while x:
            if x // div != x % 10: return False
            x = (x%div) // 10
            div /= 100
        return True