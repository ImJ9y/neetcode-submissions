class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp = sorted(list(set(nums)))

        longest = 1
        length = 1

        for i in range(len(temp)-1):
            cur = temp[i]
            if cur+1 == temp[i+1]:
                length += 1
            else:
                length = 1
            
            longest = max(longest, length)
        
        return longest