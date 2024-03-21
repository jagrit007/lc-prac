import java.util.HashMap;
import java.util.Map;

class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> count = new HashMap<>();
        int result = 0;
        int l = 0;
        
        for (int r = 0; r < s.length(); r++) {
            char currentChar = s.charAt(r);
            count.put(currentChar, count.getOrDefault(currentChar, 0) + 1);

            if ((r - l + 1) - Collections.max(count.values()) > k) {
                // Move window
                count.put(s.charAt(l), count.get(s.charAt(l)) - 1); // Firstly, remove leftmost while moving window
                l++; // Finally, move the window
            }
            
            result = Math.max(result, r - l + 1);
        }
        return result;
    }
}
