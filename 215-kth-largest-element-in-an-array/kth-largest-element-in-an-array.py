from heapq import heappop, heappush, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-e for e in nums]
        heapify(heap)
        for i in range(k-1):
            heappop(heap)
        return -1 * heappop(heap)