import java.util.Stack;

public class MinStack {
  
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> min_vals = new Stack<>();

        
        public void push(int val) {
            stack.push(val);
            if(!min_vals.empty()){
                min_vals.push(Math.min(val, min_vals.peek()));
            }else{
                min_vals.push(val);
            }
        }
        
        public void pop() {
            stack.pop();
            min_vals.pop();
        }
        
        public int top() {
            return stack.peek();
        }
        
        public int getMin() {
            return min_vals.peek();
        }
    }