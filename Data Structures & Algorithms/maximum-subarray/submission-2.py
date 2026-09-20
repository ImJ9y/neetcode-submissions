class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cur = 0
        max_cur = max(nums)
        for num in nums:
            cur += num
            max_cur = max(max_cur, cur)

            if cur < 0:
                cur = 0
            
        return max_cur
