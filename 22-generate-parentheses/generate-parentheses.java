import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        StringBuilder intermediate = new StringBuilder(2 * n);

        helper(intermediate, 0, 0, n, result);
        return result;
    }

    private void helper(StringBuilder intermediate, int left, int right, int n, List<String> result) {
        if (intermediate.length() == 2 * n) {
            result.add(intermediate.toString());
            return;
        }
        if (left < n) {
            intermediate.append('(');
            helper(intermediate, left + 1, right, n, result);
            intermediate.setLength(intermediate.length() - 1);
        }
        if (right < left) {
            intermediate.append(')');
            helper(intermediate, left, right + 1, n, result);
            intermediate.setLength(intermediate.length() - 1);
        }
    }
}
