class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, c, total):
            if total == target:
                res.append(c[:])
                return

            if i >= len(nums) or total > target:
                return

            c.append(nums[i])
            dfs(i, c, total + nums[i])
            c.pop()

            dfs(i + 1, c, total)

        dfs(0, [], 0)

        return res