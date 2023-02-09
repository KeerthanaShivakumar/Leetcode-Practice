# 2485. Find the Pivot Integer
class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            l = sum([j for j in range(1,i+1)])
            r = sum([k for k in range(i, n+1)])
            if(l==r):
                return i
                break
        return -1