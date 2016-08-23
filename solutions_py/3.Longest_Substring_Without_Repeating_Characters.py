#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:return 0;
        maxlen = 0
        char_dict = {}
        start,end = 0,0
        for i,ch in enumerate(s):
            if ch not in char_dict or char_dict[ch]<start:
                end = i
                maxlen = max(maxlen, end-start+1)
            else:
                start = char_dict[ch]+1
            char_dict[ch] = i
        return maxlen



if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abcabccc")
    print Solution().lengthOfLongestSubstring("bbbbbb")
    print Solution().lengthOfLongestSubstring("pwwkew")
    print Solution().lengthOfLongestSubstring("abc")
    print Solution().lengthOfLongestSubstring("")
