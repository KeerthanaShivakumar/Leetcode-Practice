#1742. Maximum Number of Balls in a Box
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box={}
        for i in range(lowLimit, highLimit+1):
            sumD = sum(map(int, list(str(i)))) #finding the sum of digits - faster
            if sumD not in box.keys():
                box[sumD]=1 #initial frequency
            else:
                box[sumD]+=1 #final frequency
        return(max(box.values()))
    