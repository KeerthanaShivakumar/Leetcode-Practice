#6303. Separate the Digits in an Array 
# biweekly-contest-97
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        temp_str=""
        res=[]
        for num in nums:
            temp_str+=str(num)
        for i in temp_str:
            new_i = int(i)
            res.append(new_i)
        return(res)