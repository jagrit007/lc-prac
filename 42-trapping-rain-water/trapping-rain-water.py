class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water_blocks = 0
        start_index = 0
        end_index = len(height) - 1

        while start_index < end_index:
            if height[start_index] <= height[end_index]:
                min_height = height[start_index]
                start_index += 1
                while start_index < end_index and height[start_index] < min_height:
                    water_blocks += min_height - height[start_index]
                    start_index += 1
            else:
                min_height = height[end_index]
                end_index -= 1
                while start_index < end_index and height[end_index] < min_height:
                    water_blocks += min_height - height[end_index]
                    end_index -= 1

        return water_blocks
