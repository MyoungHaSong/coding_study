class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l,r = 0,len(nums)+1
        sub = 0
        for i in range(len(nums)):
            sub += nums[i]
            while sub >= s:
                r = min(r, i-l+1)
                sub -= nums[l]
                l +=1
        return r if r != len(nums) + 1 else 0                         