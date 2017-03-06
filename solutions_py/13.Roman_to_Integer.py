#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma_reg_1 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        roma_reg_2 = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C']
        roma_reg_3 = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M']
        roma_reg_4 = ['M', 'MM', 'MMM']

        roma_reg_1.reverse()
        roma_reg_2.reverse()
        roma_reg_3.reverse()
        roma_reg_4.reverse()

        intRoman = 0
        for i, reg in enumerate(roma_reg_4):
            if s.startswith(reg):
                intRoman += (3-i)*1000
                s = s[len(reg):]
                break
        for i, reg in enumerate(roma_reg_3):
            if s.startswith(reg):
                intRoman += (10-i)*100
                s = s[len(reg):]
                break
        for i, reg in enumerate(roma_reg_2):
            if s.startswith(reg):
                intRoman += (10-i)*10
                s = s[len(reg):]
                break
        for i, reg in enumerate(roma_reg_1):
            if s.startswith(reg):
                intRoman += (10-i)*1
                s = s[len(reg):]
                break
        return intRoman


if __name__ == '__main__':
    print Solution().romanToInt("II")
    print Solution().romanToInt("IX")
    print Solution().romanToInt("XLIX")
    print Solution().romanToInt("MCMXCVI")
