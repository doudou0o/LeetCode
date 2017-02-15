#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows < 2:
            return s

        step, zigzag = 2*numRows - 2 , ""
        for i in range(numRows):
            for j in range(i, len(s), step):
                zigzag += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
        return zigzag


if __name__ == '__main__':
    print Solution().convert("a", 3)
    print Solution().convert("a", 1)
    print Solution().convert("cba", 2)
    print Solution().convert("123456789", 3)
    print Solution().convert("123456789", 5)
