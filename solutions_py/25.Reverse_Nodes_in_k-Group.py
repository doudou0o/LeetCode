#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        cur = head
        n = 0
        while cur!=None and n!=k:
            cur = cur.next
            n = n + 1

        if n==k:
            cur = self.reverseKGroup(cur, k)
            for i in range(k):
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
            return cur
        else:
            return head

if __name__ == '__main__':
    t = l1 = ListNode(1)
    ans = Solution().reverseKGroup(l1, 1)
    while ans:
        print ans.val
        ans = ans.next
    print "======"

    t = l1 = ListNode(1)
    t.next = ListNode(2);t=t.next
    ans = Solution().reverseKGroup(l1, 2)
    while ans:
        print ans.val
        ans = ans.next
    print "======"

    t = l1 = ListNode(1)
    t.next = ListNode(2);t=t.next
    t.next = ListNode(3);t=t.next
    t.next = ListNode(4);t=t.next
    t.next = ListNode(5);t=t.next
    ans = Solution().reverseKGroup(l1, 2)
    while ans:
        print ans.val
        ans = ans.next
    print "======"

    t = l1 = ListNode(1)
    t.next = ListNode(2);t=t.next
    t.next = ListNode(3);t=t.next
    t.next = ListNode(4);t=t.next
    t.next = ListNode(5);t=t.next
    ans = Solution().reverseKGroup(l1, 3)
    while ans:
        print ans.val
        ans = ans.next
    print "======"

