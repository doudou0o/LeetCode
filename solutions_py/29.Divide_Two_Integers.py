#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAXINT = 2147483647
        MININT =-2147483648
        if divisor==0:
            return MAXINT
        if dividend == MININT and divisor==-1:
            return MAXINT

        isPos = (dividend<0 and divisor<0) or (dividend>0 and divisor>0)

        dd = abs(dividend)
        dv = abs(divisor)

        digit=0
        while dd >= dv:
            dv = dv << 1
            digit += 1

        dv = dv >> digit
        digit -= 1
        ans = 0

        while digit>=0:
            if dd >= dv << digit:
                dd -= dv << digit
                ans += 1 << digit
            digit -= 1

        return ans if isPos else -ans

if __name__ == '__main__':
    print Solution().divide(2, 0)
    print Solution().divide(4, 2)
    print Solution().divide(28, 6)
    print Solution().divide(-2147483648, -1)
