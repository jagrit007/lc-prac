class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        hmap = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            if char in hmap:
                # Move the start pointer to the next index after the previous occurrence of the repeating character
                start = max(start, hmap[char] + 1)
            # Update the current character's index in the hashmap
            hmap[char] = end
            # Update the maximum length of the substring without repeating characters
            max_length = max(max_length, end - start + 1)
        
        return max_length
