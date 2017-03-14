#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        ind = 0
        for i in range(len(nums)):
            if val==nums[i]:
                continue
            nums[ind] = nums[i]
            ind = ind + 1
        return ind


if __name__ == '__main__':
    print Solution().removeElement()
