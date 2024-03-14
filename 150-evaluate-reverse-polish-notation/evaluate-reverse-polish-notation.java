import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> numStack = new Stack<>();
        int res = 0;
        for (String token : tokens) {
            if (token.equals("+")) {
                numStack.push(numStack.pop() + numStack.pop());
                continue;
            }
            if (token.equals("/")) {
                int a = numStack.pop();
                int b = numStack.pop();
                numStack.push(b / a);
                continue;
            }
            if (token.equals("*")) {
                numStack.push(numStack.pop() * numStack.pop());
                continue;
            }
            if (token.equals("-")) {
                int a = numStack.pop();
                int b = numStack.pop();
                numStack.push(b - a);
                continue;
            } else {
                numStack.push(Integer.parseInt(token));
            }
        }
        return numStack.pop();
    }
}
