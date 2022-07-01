#1299. Replace Elements with Greatest Element on Right Side - Easy
'''
Based on slicing the array
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        for i in range(n-1):
            subarray = arr[i+1::]
            arr[i]=max(subarray)
        arr[-1]=-1
        return arr
    