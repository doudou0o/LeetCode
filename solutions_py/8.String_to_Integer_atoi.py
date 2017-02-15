#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def myAtoi(self, InputStr):
        """
        :type str: InputStr
        :rtype: int
        """

        MAX_INT = (1<<31) - 1
        MIN_INT = -1*(1<<31)
        isMinus = False

        if not InputStr or not InputStr.strip():
            return 0

        InputStr = InputStr.strip()

        if InputStr.startswith("+"):
            InputStr = InputStr[1:]
        elif InputStr.startswith("-"):
            InputStr = InputStr[1:]
            isMinus = True

        result = 0
        for c in InputStr:
            if c < '0' or c > '9':
                break
            if result > (MAX_INT - int(c)) / 10:
                return MIN_INT if isMinus else MAX_INT
            result = result*10 + int(c)

        return -1*result if isMinus else result




if __name__ == '__main__':
    print Solution().myAtoi("")
    print Solution().myAtoi("0")
    print Solution().myAtoi("-1")
    print Solution().myAtoi("2147483647")
    print Solution().myAtoi("-2147483647")
    print Solution().myAtoi("2147483648")
    print Solution().myAtoi("-2147483648")

