class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_num = n
        count = 0

        while bit_num != 0:
            if bit_num & 1:
                count += 1
            bit_num >>= 1

        return count