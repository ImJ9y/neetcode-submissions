class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        cur = prices[0]
        for price in prices:
            if cur > price:
                cur = price
            
            max_price = max(max_price, price - cur)
        
        return max_price