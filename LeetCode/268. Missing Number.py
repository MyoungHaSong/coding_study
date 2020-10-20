        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(list(range(n+1)))
        return s - sum(nums)
    def missingNumber(self, nums: List[int]) -> int:
        s = [1] * (len(nums) +1 )
        for i in nums:
            s[i] = 0
        for i in range(len(s)):
            if s[i] !=0:
                return i