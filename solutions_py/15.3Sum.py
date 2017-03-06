#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []

        nums = sorted(nums)
        ansPair = []

        lastNum = None
        for i,num in enumerate(nums):
            if lastNum == num:
                continue
            else:
                lastNum = num
            if i > len(nums)-3:
                break
            pairs = self.twoSum(nums[i+1:], 0-num)
            for pair in pairs:
                ansPair.append([num, pair[0], pair[1]])

        return ansPair


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums)==0:
            return []

        i,j = 0, len(nums)-1
        ansPair = []

        while i!=j :
            cur = nums[i]+nums[j]
            if target - cur < 0:
                j = j-1
            if target - cur > 0:
                i = i+1
            if target - cur == 0:
                if len(ansPair)==0 or nums[i] != ansPair[-1][0]:
                    ansPair.append([nums[i], nums[j]])
                i = i+1


        return ansPair



if __name__ == '__main__':
    print Solution().threeSum([0,0,0,0])
    print Solution().threeSum([-1,0,1,2,-1,-4])
