class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        for i in range(len(nums1)):
            nums3.append(nums1[i])
        for j in range(len(nums2)):
            nums3.append(nums2[j])
        nums3 = sorted(nums3)
        n = len(nums3)
        if n % 2 == 1:
            median = nums3[n // 2]
        else:
            median = (nums3[n // 2 - 1] + nums3[n // 2]) / 2
        return float(median)

        