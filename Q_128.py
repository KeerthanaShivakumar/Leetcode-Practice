#128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        s=set() #hash of all elements
        ans=0 #final answer to be returned
        #add elements to hash
        for ele in nums:
            s.add(ele)
        #check for consecutive elements
        for i in range(n):
            if nums[i]-1 not in s:
                j=nums[i]
                while j in s:
                    j+=1
                ans = max(ans, j-nums[i])
        return ans