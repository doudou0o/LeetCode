#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == 0:
            return 0 if len(needle)==0 else -1

        for i in range(len(haystack)):
            for j in range(len(needle)+1):
                if (j==len(needle)): return i
                if (i+j == len(haystack)): return -1
                if (needle[j]!=haystack[i+j]):
                    break
        return -1

if __name__ == '__main__':
    print Solution().strStr("1", "1")
    print Solution().strStr("missssidddd", "1")
    print Solution().strStr("BBC ABCDAB ABCDABCDABDE", "ABCDABD")
