class Solution:
    def reverse(self, x: int) -> int:
        MAX_VAL = 2**31
        rev = 0
        isNeg = True if x < 0 else False
        x = abs(x)
        while x != 0:
            rev = (rev * 10) + (x%10)
            x = floor(x/10)
        return -rev if isNeg and -rev > -(MAX_VAL) else (0 if rev > (MAX_VAL) else rev)