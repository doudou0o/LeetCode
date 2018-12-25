#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binsearch(nums, target, 0)

    def binsearch(self, nums, target, spos):
        """
        :type nums: List[int]
        :type target: int
        :type spos: int
        :rtype: int
        """
        if not nums: return -1
        s,m,e         = 0, len(nums) / 2, len(nums)-1

        if target == nums[m]:
            return m + spos
        if target == nums[s]:
            return s + spos
        if target == nums[e]:
            return e + spos

        if nums[s] < nums[m]:
            if target > nums[s] and target < nums[m]:
                return self.binsearch(nums[s:m], target, spos+s)
            else:
                return self.binsearch(nums[m:e], target, spos+m)
        if nums[s] >= nums[m]:
            if target > nums[m] and target < nums[e]:
                return self.binsearch(nums[m:e], target, spos+m)
            else:
                return self.binsearch(nums[s:m], target, spos+s)



if __name__ == '__main__':
    print Solution().search([4,6,8,9,1,2,3], 6)
    print Solution().search([4,6,8,9,1,2,3], 3)
    print Solution().search([4,6,8,9,1,2,3], 7)
    print Solution().search([4,5,6,7,0,1,2], 0)






