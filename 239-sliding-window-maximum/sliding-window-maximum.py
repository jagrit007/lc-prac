from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        result = []
        window = deque()
        
        for i in range(len(nums)):
            while window and window[0] < i - k + 1:
                window.popleft() #moving the window
            
            
            while window and nums[window[-1]] < nums[i]:
                window.pop() #remove elements smaller than nums[i] from the deque, keep the max of this window only
            
            
            window.append(i) # add current index to the window
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result
