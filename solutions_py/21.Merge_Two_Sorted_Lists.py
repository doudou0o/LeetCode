#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        cur  = head

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2

        return head.next

if __name__ == '__main__':
    l1 = ListNode(1);
    f = l1
    f.next = ListNode(3); f = f.next;
    f.next = ListNode(5); f = f.next;
    f.next = ListNode(6); f = f.next;
    f.next = ListNode(6); f = f.next;
    f.next = ListNode(8); f = f.next;

    l2 = ListNode(2);
    f = l2
    f.next = ListNode(3); f = f.next;
    f.next = ListNode(4); f = f.next;
    f.next = ListNode(6); f = f.next;
    f.next = ListNode(7); f = f.next;
    f.next = ListNode(9); f = f.next;
    f.next = ListNode(9); f = f.next;
    f.next = ListNode(11); f = f.next;

    ans = Solution().mergeTwoLists(l1, l2)
    while ans!=None:
        print ans.val
        ans = ans.next

