class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)  # Append a zero height at the end to ensure all elements in the stack are popped at the end
        
        max_area = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top_index = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top_index] * width)

        return max_area
