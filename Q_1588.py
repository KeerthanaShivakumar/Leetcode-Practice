# 1588. Sum of All Odd Length Subarrays
# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res=0
        for i in range(n):
            res += ((((i + 1) *(n - i) +1) // 2) * arr[i])
        return res