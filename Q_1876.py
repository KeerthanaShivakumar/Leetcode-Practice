#1876. Substrings of Size Three with Distinct Characters
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res=[]
        for i in range(len(s)):
            if(len(s[i: i+3])==3 and len(s[i: i+3])==len(set(s[i: i+3]))):
                res.append(s[i: i+3])
        return len(res)