#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binsearch(nums, target)
        pass

    def binsearch(self, nums, target):
        if not nums:
            return 0
        s,m,e = 0, len(nums)/2, len(nums)-1
        if target == nums[s] or target < nums[s]:
            return s
        if target == nums[e]:
            return e
        if target > nums[e]:
            return e+1
        if target == nums[m]:
            return m
        if target > nums[m]:
            return m + self.binsearch(nums[m:e], target)
        if target < nums[m]:
            return s + self.binsearch(nums[s:m], target)

if __name__ == '__main__':
    print Solution().searchInsert([1,3,5,6], 5)
    print Solution().searchInsert([1,3,5,6], 2)
    print Solution().searchInsert([1,3,5,6], 7)
    print Solution().searchInsert([1,3,5,6], 0)
