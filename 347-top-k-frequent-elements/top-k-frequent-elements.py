class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = collections.Counter(nums)
        heap = [(v, k) for k,v in _dict.items()]
        heapify(heap)
        while len(heap) > k:
            heappop(heap)
        # return [x for (freq, x) in heap]
        return [x[1] for i,x in enumerate(heap, start=1) if i<=k]