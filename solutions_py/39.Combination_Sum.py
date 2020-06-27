#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates, minCand = set(candidates), min(candidates)
        result = []

        self.combination(candidates, minCand, target, [], result)

        #for cand in candidates:
        #    if cand > target:
        #        continue
        #    num,x = 1,cand
        #    while target - x >= 0:
        #        if target - x == 0:
        #            result.append([cand] * num)
        #            break
        #        if  target-x in candidates:
        #            result.append([cand] * num + [target-x])
        #        num, x = num+1, x + cand

        return result
        #return self.unique(result)

    def combination(self, candidates, minCand, target, ret, result):
        if target in candidates:
            result.append(ret+[target])
        if target < minCand:
            return
        for cand in candidates:
            ret.append(cand)
            self.combination(candidates, minCand, target-cand, ret, result)
            ret.pop()
        return

    def unique(self, rets):
        unique_list = set()
        results = []
        for ret in rets:
            line = str(sorted(ret))
            if line not in unique_list:
                unique_list.add(line)
                results.append(ret)
        return results 



if __name__ == '__main__':
    print(Solution().combinationSum([2,3,4,5,6,7], 7))
    print(Solution().combinationSum([2,3,5], 8))
    print(Solution().combinationSum([7,3,2], 18))
