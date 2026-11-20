class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        res = nums[0]

        while L <= R:
            if nums[L] <= nums[R]:
                res = min(res, nums[L])
                break

            M = (L+R)//2
            res = min(res, nums[M])

            if nums[M] < nums[R]:
                R = M - 1
            else:
                L = M + 1
        
        return res