class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        R = 0
        cur = 0
        total = float('-inf')

        for num in nums:
            cur += num
            total = max(total, cur)
            if cur < 0:
                cur = 0

        return total