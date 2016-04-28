#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        num_dict = {}
        for (i,num) in enumerate(nums):
            need = target - num
            if need in num_dict:
                return [num_dict[need],i]
            else:
                num_dict[num] = i

if __name__ == '__main__':
    num_list = [2,7,11,15]
    target = 9

    print Solution().twoSum(num_list, target)
