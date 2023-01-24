# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix=""
        strs.sort()
        first_ele = strs[0]
        last_ele=strs[-1]
        for i in range(min(len(first_ele), len(last_ele))):
            if(first_ele[i]==last_ele[i]):
                longest_prefix = longest_prefix+first_ele[i]
            else:
                break
        return longest_prefix