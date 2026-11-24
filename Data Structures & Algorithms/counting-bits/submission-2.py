class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(n):
            count = 0

            while n:
                if n & 1 == 1:
                    count += 1
                n >>= 1
            
            return count

        res = []
        res.append(0)

        for i in range(1, n+1):
            res.append(helper(i))
        
        return res

