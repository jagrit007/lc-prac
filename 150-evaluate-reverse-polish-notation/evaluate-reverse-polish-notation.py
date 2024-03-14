class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        op_stack = []
        res = 0
        for i in tokens:
            if i == "+":
                num_stack.append(num_stack.pop() + num_stack.pop())
                continue
            if i == "/":
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(int(b / a))
                continue
            if i == "*":
                num_stack.append(num_stack.pop() * num_stack.pop())
                continue
            if i == "-":
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(b - a)
                continue
            else:
                num_stack.append(int(i))
        return int(num_stack[0])      


        