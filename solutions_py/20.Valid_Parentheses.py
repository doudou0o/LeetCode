#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for c in s:
            if c in '([{':
                stack.append(c)
            if c in ')]}':
                if len(stack)==0 or stack.pop()+c not in ["()","[]","{}"]:
                    return False

        return len(stack)==0

if __name__ == '__main__':
    print Solution().isValid("()[]{}")
    print Solution().isValid("([)]")
    print Solution().isValid("(")
    print Solution().isValid(")")

