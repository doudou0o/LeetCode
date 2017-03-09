#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(curStr, left, right, strList):
            if left:
                generate(curStr+"(", left-1, right, strList)
            if right and right-left>0:
                generate(curStr+")", left, right-1, strList)
            if right==0:
                strList.append(curStr)

        ret = []
        generate("", n, n, ret)
    
        return ret

if __name__ == '__main__':
    print Solution().generateParenthesis(3)
