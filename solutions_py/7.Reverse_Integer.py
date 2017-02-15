#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        isMinus = True if x < 0 else False 
        x = -x if x < 0 else x
        ans = 0
        while x!=0:
            tempAns = ans*10 + x%10
            if tempAns<0 or tempAns/10<ans or tempAns>(1<<31)-1:
                return 0
            ans = tempAns
            x = x/10
        return -ans if isMinus else ans




if __name__ == '__main__':
    print Solution().reverse(1)
    print Solution().reverse(0)
    print Solution().reverse(-1)
    print Solution().reverse(123)
    print Solution().reverse(-123)
    print Solution().reverse(-12)
    print Solution().reverse(1534236469)

