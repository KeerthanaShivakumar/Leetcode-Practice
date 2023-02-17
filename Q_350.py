# 350. Intersection of 2 arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort and then use 2 pointers
        a = 0
        b = 0
        res = []
        nums1.sort()
        nums2.sort()
        while ((a < len(nums1)) and (b < len(nums2))):
            if (nums1[a] < nums2[b]):
                a = a+1
            elif (nums1[a] > nums2[b]):
                b = b+1
            else:
                res.append(nums1[a])
                a = a+1
                b = b+1
        return res
