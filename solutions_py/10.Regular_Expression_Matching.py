#!/usr/bin/env python
# -*- coding: utf-8 -*-

### 递归
class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p=="":
            return s==""

        if len(p)>1 and '*' == p[1]:
            return self.isMatch(s, p[2:]) or ((s!="" and (s[0]==p[0] or '.'==p[0])) and self.isMatch(s[1:], p))
        else:
            return (s!="" and (s[0]==p[0] or '.'==p[0])) and self.isMatch(s[1:], p[1:])

### DP
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens = len(s)
        lenp = len(p)
        dp = [[False for col in range(lenp+1)] for row in range(lens+1)]
        dp[0][0] = True

        for j in range(1, lenp+1):
            dp[0][j] = p[j-1]=='*' and dp[0][j-2]==1

        for i in range(1, lens+1):
            for j in range(1, lenp+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1]==p[j-2] or '.'==p[j-2]))
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or '.'==p[j-1])

        return dp[lens][lenp]



if __name__ == '__main__':
    print Solution().isMatch("aab", "c*a*b")
    print Solution().isMatch("a","a*")
    print Solution().isMatch("","a*")
    print Solution().isMatch("ccd","a*c*d")
    print Solution().isMatch("aaaa","ab*a*c*a")


