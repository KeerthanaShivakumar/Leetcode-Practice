# 2455. Average Value of Even Numbers That Are Divisible by Three
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res=[]
        for ele in nums:
            if(ele%2==0 and ele%3==0):
                res.append(ele)
        if(res!=[]):
            return(sum(res)//len(res))
        else:
            return 0