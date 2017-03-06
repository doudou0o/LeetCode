#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""

        prefix = strs[0]
        for s in strs:
            tempPrefix = ""
            for i in range(min(len(s), len(prefix))):
                if s[i] == prefix[i]:
                    tempPrefix += s[i]
                else:
                    break
            prefix = tempPrefix

        return prefix


if __name__ == '__main__':
    print Solution().longestCommonPrefix(["abcvd", "abcdd", "ab"])
    print Solution().longestCommonPrefix(["abcd"])
    print Solution().longestCommonPrefix(["aaa", "aaaaa", "a"])
