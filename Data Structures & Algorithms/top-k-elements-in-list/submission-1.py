class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}

        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        
        res = []
        num_map = sorted(num_map.items(), key = lambda item:item[1], reverse=True)

        for num, count in num_map:
            if k > 0:
                k -= 1
                res.append(num)
        
        return res