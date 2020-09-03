class Solution:
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target :
                    return [i,j]

class Solution:
    def twoSum(self, nums,target):
        dic = {}
        for i,n in enumerate(nums):
            dif = target - n
            if dif not in dic:
                dic[n] = i
            else:
                return [dic[dif],i]
            
