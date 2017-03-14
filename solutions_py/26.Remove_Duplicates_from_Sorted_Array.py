#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ind = 0
        for i in range(len(nums)):
            if ind>0 and nums[ind-1]==nums[i]:
                continue
            nums[ind] = nums[i]
            ind = ind + 1
            pass

        return ind


if __name__ == '__main__':
    print Solution().removeDuplicates([1,2])
    print Solution().removeDuplicates([1,1,2,3,3,4])
    print Solution().removeDuplicates([1,1,2])
    print Solution().removeDuplicates([1,1,1])
    print Solution().removeDuplicates([1])
    print Solution().removeDuplicates([])
