#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitsMap = {
                '2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz',
                '*':'+',
                '0':' ',
                }

        ansList = []
        candList = [""]
        for c in digits:
            ansList = []
            for cand in candList:
                for ch in digitsMap[c]:
                    ansList.append(cand+ch)
            candList = ansList

        return ansList

if __name__ == '__main__':
    print Solution().letterCombinations("23")

