#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                i = i - 1
                break
        else:
            nums.reverse()
            return

        for j in range(len(nums)-1, i-1, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break

        suffix = nums[i+1:]; suffix.reverse()
        nums[i+1:] = suffix
        #print nums
        return



if __name__ == '__main__':
    print Solution().nextPermutation([1,2,3]) #1,3,2
    print Solution().nextPermutation([3,2,1]) #1,2,3
    print Solution().nextPermutation([1,1,5]) #1,5,1


