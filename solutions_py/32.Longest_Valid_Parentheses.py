#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = 'X'+s
        dp = [0]*len(s)

        for i in range(len(s)):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            if s[i] == ')' and s[i-1] == ')':
                if s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1] + dp[i-1-dp[i-1]-1] + 2
        print dp
        return max(dp)



if __name__ == '__main__':
    print Solution().longestValidParentheses("((()(())(()")
    print Solution().longestValidParentheses(")(")
    print Solution().longestValidParentheses("()()")


