#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_x = str(x)
        str_y = str_x[::-1]

        for i in range(len(str_x)):
            if str_x[i] != str_y[i]:
                return False
        return True

if __name__ == '__main__':
    print Solution().isPalindrome(2)
    print Solution().isPalindrome(121)
    print Solution().isPalindrome(1221)
    print Solution().isPalindrome(1121)

