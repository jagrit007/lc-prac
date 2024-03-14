class Solution:
    def isPalindrome(self, str, i, j):
        while i < j:
            if str[i] != str[j]:
                return False
            i +=1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []
        intermediate = []

        def helper(i):
            if i >= len(s):
                result.append(intermediate.copy())
                return
            for k in range(i, len(s)):
                if self.isPalindrome(s, i, k):
                    intermediate.append(s[i:k+1])
                    helper(k+1)
                    intermediate.pop()
        helper(0)
        return result