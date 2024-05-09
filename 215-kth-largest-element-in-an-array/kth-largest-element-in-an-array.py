from heapq import heappop, heappush, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapify(heap)
        for _ in range(1,k):
            heappop(heap)
        return -heappop(heap)