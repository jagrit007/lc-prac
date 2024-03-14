import java.util.Stack;
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> maxStack = new ArrayDeque<>(); // store indexes
        int[] result = new int[temperatures.length];
        
        for (int i = 0; i < temperatures.length; i++) {
            int temp = temperatures[i];
            while (!maxStack.isEmpty() && temp > temperatures[maxStack.peekLast()]) {
                int prevDay = maxStack.removeLast();
                result[prevDay] = i - prevDay;
            }
            maxStack.addLast(i);
        }
        
        return result;
    }

    public int[] dailyTemperatures2(int[] temperatures) {
        Stack<Integer> maxStack = new Stack<>(); // store indexes
        int[] result = new int[temperatures.length];
        
        for (int i = 0; i < temperatures.length; i++) {
            int temp = temperatures[i];
            while (!maxStack.isEmpty() && temp > temperatures[maxStack.peek()]) {
                int prevDay = maxStack.pop();
                result[prevDay] = i - prevDay;
            }
            maxStack.push(i);
        }
        
        return result;
    }
}
