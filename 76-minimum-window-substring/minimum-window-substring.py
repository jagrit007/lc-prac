class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        if not s or not t:
            return result

        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1
        
        i = 0
        min_len = float('inf')
        _map = defaultdict(int)
        
        for j in range(len(s)):
            if s[j] in t_map:
                _map[s[j]] += 1

                # if _map == t_map:
                while self.contains_all(_map, t_map):
                    new_len = j - i + 1
                    if new_len < min_len:
                        min_len = new_len
                        result = s[i:j+1]

                    # Move the left pointer to minimize window
                    if s[i] in t_map:
                        _map[s[i]] -= 1
                    i += 1
        return result
                
    def contains_all(self, _map, t_map):
        for key in t_map:
            if _map[key] < t_map[key]:
                return False
        return True