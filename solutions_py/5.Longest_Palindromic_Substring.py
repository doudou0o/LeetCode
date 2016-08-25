#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # proprecess
        news = "#"+ "#".join([x for x in s]) +"#"
        maxp = 1; pos = 0;
        
        pld = [0]*len(news)
        cur = 0; right = 0;
        for i in xrange(len(news)):
            mirror = 2*cur - i
            pld[i] = min(right-i, pld[mirror]) if i < right else 0

            while( (i+pld[i]+1)<len(news) and (i-pld[i]-1)>=0 and news[i+pld[i]+1]==news[i-pld[i]-1] ):
                pld[i] += 1

            if i+pld[i] > right:
                right = i+pld[i]
                cur = i

            if pld[i] > maxp:
                maxp = pld[i]
                pos  = i
        pass
        print pos, maxp
        return s[ (pos+1-maxp)/2 : (pos+1+maxp)/2]

if __name__ == '__main__':
    print Solution().longestPalindrome("a")
    print Solution().longestPalindrome("aa")
    print Solution().longestPalindrome("aaa")
    print Solution().longestPalindrome("aabbac")
    print Solution().longestPalindrome("abcbabcbccxxxx")
    print Solution().longestPalindrome("babcbabcbaccba")
