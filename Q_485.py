# 485. Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        count=0
        for ele in nums:
            if(ele==0):
                count=0
            else:
                count+=1
                res = max(res,count)
        return res
