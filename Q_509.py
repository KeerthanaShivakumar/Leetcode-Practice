#Fibonacci number - Easy
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        fiba=0
        fibb=1
        fibi=0
        for i in range(1,n):
            fibi=fiba+fibb
            fiba=fibb
            fibb=fibi
        return fibi