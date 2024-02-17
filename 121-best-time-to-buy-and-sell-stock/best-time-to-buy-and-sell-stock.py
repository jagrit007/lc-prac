class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_highest = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                curr_highest = max(curr_highest, prices[r] - prices[l])
            else:
                l=r
            r+=1
        return curr_highest
                        
