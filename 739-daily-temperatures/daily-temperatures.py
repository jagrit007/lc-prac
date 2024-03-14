class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_stack = [] # store indexes
        result = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while max_stack and temp > temperatures[max_stack[-1]]:
                prev_day = max_stack.pop()
                result[prev_day] = i - prev_day
            max_stack.append(i)
            
        return result