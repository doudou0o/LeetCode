#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s,e = self.binsearch(nums, target, 0)
        if s is None:
            return [-1,-1]
        return [s,e]

    def binsearch(self, nums, target, spos):
        """
        :type nums: List[int]
        :type target: int
        :type spos: int
        :rtype: List[int]
        """
        if not nums:
            return [None, None]
        if len(nums) == 1:
            if nums[0] == target:
                return [spos,spos]
            else:
                return [None,None]


        s,m,e = 0,len(nums)/2,len(nums)-1
        if target < nums[m]:
            return self.binsearch(nums[s:m], target, spos+s)
        if target > nums[m]:
            return self.binsearch(nums[m:e+1], target, spos+m)
        if target == nums[m]:
            left  = self.binsearch_left(nums[s:m+1], target, spos+s)
            right = self.binsearch_right(nums[m:e+1], target, spos+m)
            return [left,right]

    def binsearch_left(self, nums, target, spos):
        if not nums:
            return None
        if nums[0] == target:
            return spos
        if len(nums) == 2:
            if nums[1] == target:
                return spos + 1
            else:
                return None

        s,m,e = 0,len(nums)/2,len(nums)-1
        if target == nums[m]:
            return self.binsearch_left(nums[s:m+1], target, spos+s)
        if target > nums[m]:
            return self.binsearch_left(nums[m:e+1], target, spos+m)
        pass

    def binsearch_right(self, nums, target, spos):
        if not nums:
            return None
        if nums[-1] == target:
            return spos + len(nums)-1
        if len(nums) == 2:
            if nums[0] == target:
                return spos
            else:
                return None

        s,m,e = 0,len(nums)/2,len(nums)-1
        if target == nums[m]:
            return self.binsearch_right(nums[m:e+1], target, spos+m)
        if target < nums[m]:
            return self.binsearch_right(nums[s:m+1], target, spos+s)
        pass

if __name__ == '__main__':
    #print Solution().searchRange([8],8)
    #print Solution().searchRange([1,8],8)
    #print Solution().searchRange([1,8],1)
    print Solution().searchRange([5,7,7,8,8,10],8)
    print "expect: 3,4"
    print Solution().searchRange([5,8,8,8,8,8,8],8)
    print "expect: 1,6"
    print Solution().searchRange([8,8,8,8,8,8,8],8)
    print "expect: 0,6"
    print Solution().searchRange([8,8,8,8,8,9,9],8)
    print "expect: 0,4"
    print Solution().searchRange([5,7,7,8,8,10],9)
    print "expect: -1,-1"



