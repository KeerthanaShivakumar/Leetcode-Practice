# 1979. Find Greatest Common Divisor of Array
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        biggest = max(nums)
        smallest = min(nums)
        #code for gcd
        while(smallest>0 and biggest>0):
            if(smallest>biggest):
                smallest = smallest%biggest
            else:
                biggest=biggest%smallest
        if(smallest==0):
            return biggest
        else:
            return smallest