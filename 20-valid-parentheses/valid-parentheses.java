import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> hm = new HashMap<>();
        hm.put('}', '{');
        hm.put(']', '[');
        hm.put(')', '(');
        // iterate over string and push to stack
        int i = 0;
        while(i < s.length()){
            if(s.charAt(i) == (char) '}' || s.charAt(i) == ']' || s.charAt(i) == ')'){
                if(stack.empty()){return false;}
                System.out.println(hm.get(s.charAt(i)));
                if(stack.peek() == hm.get(s.charAt(i))){
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else{
                stack.push(s.charAt(i));
            }
            i++;
        }
            if(stack.size() == 0){
                return true;
            }
            return false;

        }
    }