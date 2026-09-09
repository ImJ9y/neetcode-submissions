class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]

        for i in range(1, n +1):
            dp.append(dp[i//2] + i%2)
        
        return dp

        # 0 - 0
        # 1 - 01
        # 2 - 10
        # 3 - 11
        # 4 - 100
        # 5 - 101
        # 6 - 110