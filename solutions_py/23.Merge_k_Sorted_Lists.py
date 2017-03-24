#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        import pdb; pdb.set_trace()
        t = retList = ListNode(0)
        heap = []

        for node in lists:
            if node:
                heapq.heappush(heap, self.buildTuple(node))

        while len(heap)>0:
            minnode = heapq.heappop(heap)[1]
            t.next = minnode
            t = t.next
            if minnode.next != None:
                heapq.heappush(heap, self.buildTuple(minnode.next))

        return retList.next

    def buildTuple(self, node):
        return (node.val, node)


if __name__ == '__main__':

    Solution().mergeKLists([[]])

    l=[]

    l1 = t = ListNode(0); l.append(l1)
    t.next = ListNode(2); t=t.next
    t.next = ListNode(6); t=t.next
    t.next = ListNode(8); t=t.next

    l2 = t = ListNode(1); l.append(l2)
    t.next = ListNode(3); t=t.next
    t.next = ListNode(4); t=t.next
    t.next = ListNode(4); t=t.next

    l3 = t = ListNode(3); l.append(l3)
    t.next = ListNode(5); t=t.next
    t.next = ListNode(5); t=t.next
    t.next = ListNode(7); t=t.next

    ans = Solution().mergeKLists(l)
    while ans!=None:
        print ans.val
        ans=ans.next

