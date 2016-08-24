#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if (m+n) & 0x1:
            return float(self.findKSortedArrays(nums1, nums2, (m+n)/2+1))
        else:
            return float(self.findKSortedArrays(nums1,nums2,(m+n)/2)+self.findKSortedArrays(nums1,nums2,(m+n)/2+1))/2

    def findKSortedArrays(self, nums1, nums2, K):
        if len(nums1) > len(nums2):
            return self.findKSortedArrays(nums2, nums1, K)
        if len(nums1) == 0:
            return nums2[K-1]
        if K == 1:
            return min(nums1[0], nums2[0])

        p1 = min(K/2, len(nums1))
        p2 = K-p1
        p1 = p1 -1
        p2 = p2 -1

        if nums1[p1] > nums2[p2]:
            nums2 = nums2[p2+1:]
            return self.findKSortedArrays(nums1, nums2, K-(p2+1))
        elif nums1[p1] < nums2[p2]:
            nums1 = nums1[p1+1:]
            return self.findKSortedArrays(nums1, nums2, K-(p1+1))
        elif nums1[p1] == nums2[p2]:
            return nums1[p1]
        else:
            pass


if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1,3],[2])
    print Solution().findMedianSortedArrays([1,2],[3,4])
