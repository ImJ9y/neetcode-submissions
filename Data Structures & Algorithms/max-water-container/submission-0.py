class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_contain = 0

        L, R = 0, len(heights)-1

        while L < R:
            cur = 0
            if heights[L] < heights[R]:
                cur = min(heights[L], heights[R]) * (R - L)
                L += 1
            else:
                cur = min(heights[L], heights[R]) * (R - L)
                R -= 1
            
            max_contain = max(max_contain, cur)
        
        return max_contain