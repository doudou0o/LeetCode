#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roma = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}

if __name__ == '__main__':
    print Solution().intToRoman(48)
    print Solution().intToRoman(22)

