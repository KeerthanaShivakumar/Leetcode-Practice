# 1523. Count odd numbers in an interval range
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # brute force approach
        # count=0
        # for ele in range(low, high+1):
        #     if(ele%2!=0):
        #         count+=1
        # return count

        # instead use approach that has fixed formula for conditions
        if low % 2 != 0:
            if high % 2 != 0:
                return (high - low) // 2 + 1
            else:
                return (high - low) // 2 + 1
        else:
            if high % 2 != 0:
                return (high - low) // 2 + 1
            else:
                return (high - low) // 2
