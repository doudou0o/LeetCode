#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roma_reg_1 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        roma_reg_2 = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C']
        roma_reg_3 = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M']
        roma_reg_4 = ['M', 'MM', 'MMM']

        RomaStr = ""

        n_4 = num/1000 - 1
        if n_4 >= 0: RomaStr += roma_reg_4[n_4]
        n_3 = (num%1000)/100 - 1
        if n_3 >= 0: RomaStr += roma_reg_3[n_3]
        n_2 = (num%100)/10 - 1
        if n_2 >= 0: RomaStr += roma_reg_2[n_2]
        n_1 = num%10 - 1
        if n_1 >= 0: RomaStr += roma_reg_1[n_1]

        return RomaStr



class Solution1(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        val  = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman= ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        RomaStr = ""
        while num!=0:
            for i in range(len(val)):
                if num >= val[i]:
                    RomaStr += roman[i]
                    num = num - val[i]
                    break
        return RomaStr

if __name__ == '__main__':
    print Solution().intToRoman(48)
    print Solution().intToRoman(22)
    print Solution1().intToRoman(48)
    print Solution1().intToRoman(22)

