#135. Candy
'''
Approach - find the number of candies from left to right once and from right to left once
Splitting the problem into 2 parts and then merging (divide and conquer)
Neighbours in this case are the elements on left and right side.
Take the max of the values (worst case) and also because the elements with higher rating will have greater number of candies
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        #Initializing
        candiesL = [1]*n 
        candiesR = [1]*n
        candies = [1]*n
        #left neighbour check
        for i in range(0, n-1):
            #current element is ratings[i+1]
            if(ratings[i+1]>ratings[i]):
                candiesL[i+1]=candiesL[i]+1
        #right neighbour check
        for j in range(n-2, -1, -1):
            if(ratings[j]>ratings[j+1]):
                candiesR[j] = candiesR[j+1]+1
        for k in range(n):
            candies[k] = max(candiesR[k], candiesL[k])
        return(sum(candies)) #min no. of candies