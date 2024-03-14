import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        List<String> intermediate = new ArrayList<>();

        helper(s, 0, intermediate, result);
        return result;
    }

    private void helper(String s, int i, List<String> intermediate, List<List<String>> result) {
        if (i >= s.length()) {
            result.add(new ArrayList<>(intermediate));
            return;
        }
        for (int k = i; k < s.length(); k++) {
            if (isPalindrome(s, i, k)) {
                intermediate.add(s.substring(i, k + 1));
                helper(s, k + 1, intermediate, result);
                intermediate.remove(intermediate.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String str, int i, int j) {
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
