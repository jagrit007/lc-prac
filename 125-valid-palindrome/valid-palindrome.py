class Solution:
    def isPalindrome(self, s: str) -> bool:
        org_str = ''.join([x for x in s.lower() if (ord(x) >= 97 and ord(x) <=122) or x.isnumeric()])
        return org_str == org_str[::-1]