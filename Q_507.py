# 507. Perfect Number
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        #Brute force
        # res=0
        # for i in range(1, num):
        #     if(num%i==0):
        #         res=res+i
        # return(res==num)
        # sum = 1
        return num in {6, 28, 496, 8128, 33550336} #hardcoded solution