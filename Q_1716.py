#1716. Calculate Money in Leetcode Bank - Easy
class Solution:
    def totalMoney(self, n: int) -> int:
        res=0 #end result to be returned
        base=[1,2,3,4,5,6,7] #Base case
        if n<=7:
            res = sum(base[0:n])
        else:
            weekNo = (n//7) #Find the week number
            weekDay = n%7 #Find which day of the week it is
            res = sum(base) #Initial condition when n>7
            for i in range(2,weekNo+1): #for the weeks after that
                base = [x+1 for x in base] #increase the amount by 1
                res = res+sum(base) #find the total of all those weeks
            finalBase = [x+1 for x in base] #come to that week where the day lies
            res = res+sum(finalBase[0:weekDay]) #find the sum from day 1 to that day of the week
        return(res)
    