class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        pre = prices[0]
        for price in prices:
            if pre > price:
                pre = price
            else:
                total = max(total, price - pre)
        
        return total