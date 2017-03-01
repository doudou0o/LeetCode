#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0, len(height)-1
        maxA = 0
        while i!=j:
            area = (j-i) * min(height[i], height[j])
            if area > maxA:
                maxA = area
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return maxA

if __name__ == '__main__':
    print Solution().maxArea([1,2,1,3,2,1,3,1])
    print Solution().maxArea([1,2,1,2,1])

