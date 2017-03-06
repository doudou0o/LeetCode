#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        closest_sum = None

        for i,num in enumerate(nums):
            if i > len(nums)-3:
                break
            twosum_closest = self.twoSumClosest(nums[i+1:], target-num)
            if closest_sum==None or abs(target - twosum_closest-num) < abs(target-closest_sum):
                closest_sum = twosum_closest+num

        return closest_sum


    def twoSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i,j = 0, len(nums)-1
        closest_sum = None

        while i!=j :
            cur = nums[i]+nums[j]
            if target - cur < 0:
                j = j-1
                if closest_sum==None or abs(target-cur) < abs(target-closest_sum):
                    closest_sum = cur
            if target - cur > 0:
                i = i+1
                if closest_sum==None or abs(target-cur) < abs(target-closest_sum):
                    closest_sum = cur
            if target - cur == 0:
                return cur

        return closest_sum

if __name__ == '__main__':
    print Solution().threeSumClosest([0,0,0,0], 2)
    print Solution().threeSumClosest([-1,0,1,2,-1,-4], 1)
    print Solution().threeSumClosest([-1,2,1,-4], 1)

