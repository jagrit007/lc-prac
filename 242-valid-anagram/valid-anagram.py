class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) == len(s):
            for i in s:
                if i in t:
                    t = t.replace(i, '', 1)
            if len(t) == 0:
                return True
        return False

    # Alternatively can make use of two hashmaps and compare them at the end