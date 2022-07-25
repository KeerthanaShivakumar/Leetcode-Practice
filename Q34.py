# 34. Find first and last position of element in sorted array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if(nums != [] and target in nums):
            # index returns only the first position of the element in the array if found
            firstPos = nums.index(target)
            res.append(firstPos)
            # Find the number of this element in the array
            targetNo = nums.count(target)
            # print(targetNo)
            lastPos = firstPos + targetNo - 1  # How to find the last index
            res.append(lastPos)

        if(nums == [] or target not in nums):
            firstPos = -1
            lastPos = -1
            res.append(firstPos)
            res.append(lastPos)
        return res
