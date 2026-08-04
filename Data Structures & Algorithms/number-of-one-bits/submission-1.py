class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        number = (int(str(n)))

        while number:
            if number%2 != 0:
                count += 1
            number = number//2

        return count