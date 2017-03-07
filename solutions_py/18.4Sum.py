#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        ansList = []

        lastNum = None
        for i,num in enumerate(nums):
            if num==lastNum:
                continue
            else:
                lastNum=num
            if i > len(nums)-4:
                break

            threeList = self.threeSum(nums[i+1:], target-num)
            for th in threeList:
                ansList.append([num, th[0], th[1], th[2]])

        return ansList

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ansList = []

        lastNum = None
        for i,num in enumerate(nums):
            if num==lastNum:
                continue
            else:
                lastNum=num
            if i > len(nums)-3:
                break
            twoList = self.twoSum(nums[i+1:], target-num)
            for tw in twoList:
                ansList.append([num, tw[0], tw[1]])

        return ansList

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ansList=[]
        i,j = 0, len(nums)-1

        while i!=j:
            cur = nums[i]+nums[j]
            if target - cur > 0:
                i = i+1
            if target - cur < 0:
                j = j-1
            if target - cur ==0:
                if len(ansList)==0 or nums[i] != ansList[-1][0]:
                    ansList.append([nums[i], nums[j]])
                i = i+1

        return ansList


if __name__ == '__main__':
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)

