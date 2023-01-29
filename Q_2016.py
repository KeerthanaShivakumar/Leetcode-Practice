# 2016. Maximum Difference Between Increasing Elements
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        #2 loops method
        diff=-1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[j]!=nums[i] and nums[j]-nums[i]>diff):
                    diff=nums[j]-nums[i]
        return diff