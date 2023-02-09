# 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #use hash table
        hash = dict()
        for ele in nums:
            hash[ele]=0
        for ele in nums:
            hash[ele]+=1
        #find single element
        for ele in nums:
            if(hash[ele]==1):
                return(ele)
                break