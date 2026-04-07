class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in nums:
            if i == 1:
                count +=1
                res = max(count, res)
            else:
                count = 0
        return res