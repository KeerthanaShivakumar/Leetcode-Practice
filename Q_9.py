#9 - Palindrome number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rem = 0
        res = 0
        while(x>0):
            rem = x%10
            res = (res*10)+rem
            x = x//10
        return (res==original)