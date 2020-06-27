#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        a = ["1"]
        for i in range(1,n):
            a.append(self.say(a[i-1]))
        return a[-1]
    
    def say(self, line):
        c,l,ret = line[0],1,[]
        for a in line[1:]:
            if a == c:
                l = l+1
            else:
                ret.append(str(l)+c)
                c,l = a,1
        ret.append(str(l)+c)
        return "".join(ret)

if __name__ == '__main__':
    print(Solution().countAndSay(1))
    print(Solution().countAndSay(2))
    print(Solution().countAndSay(3))
    print(Solution().countAndSay(4))
    print(Solution().countAndSay(5))
    print(Solution().countAndSay(6))



