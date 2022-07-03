#376. Wiggle Subsequence - Medium
'''
Approach used - Signum function
Take the signum of the difference of consecutive elements 
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        lastSign = 0 #initial sign is 0 (begin)
        length = 1 #arbitrary length of subsequence
        for i in range(1, len(nums)): 
            diff = (nums[i]-nums[i-1]) #find difference to know nature of sequence
            if(diff>0):
                sign=1
            elif(diff<0):
                sign=-1
            else:
                sign=0
            if(sign!=lastSign and sign!=0): #best way to find alternating nature instead of taking values
                #implemented signum fn using 3 if statements above
                #sign!=lastSign indicates that the consecutive elements are not increasing or decreasing
                #sign!=0 indicates that the elements are not the same
                lastSign = sign
                length+=1 #increase length of subsequence
        return length
    