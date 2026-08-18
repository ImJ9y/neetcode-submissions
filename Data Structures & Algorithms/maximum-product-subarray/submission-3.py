class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        cur_min = 0
        cur_max = 0
        max_prod = 0

        for num in nums:
            temp = cur_max
            cur_max = max(num*cur_max, num*cur_min, num)
            cur_min = min(num*cur_min, num, num*temp)

            max_prod = max(max_prod, cur_max)
        
        return max_prod