#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        t = newHead = ListNode(0)
        t.next = head

        while t!=None and t.next!=None and t.next.next!=None:
            tmp = t.next.next
            t.next.next = tmp.next
            tmp.next = t.next
            t.next = tmp

            t = t.next.next

        return newHead.next



if __name__ == '__main__':
    t = l1 = ListNode(1)
    t.next = ListNode(2); t=t.next;
    t.next = ListNode(3); t=t.next;
    t.next = ListNode(4); t=t.next;
    t.next = ListNode(5); t=t.next;

    ans = Solution().swapPairs(l1)

    while ans!=None:
        print ans.val
        ans = ans.next

