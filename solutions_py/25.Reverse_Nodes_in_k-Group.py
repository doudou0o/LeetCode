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
        h = newhead = ListNode(0);
        cur = t = head

        for i in range(1,k):
            step = step.next if step!=None else None
        if step==None:
            return head

        num = 0
        while step!=None and cur!=None:
            ## 前插
            tmp = cur.next
            cur.next, h.next = h.next, cur

            cur, step = tmp, step.next if step!=None else None
            num = num + 1
            if num==k:
                if step == None:
                    t.next = cur
                    break
                else:
                    h, t, num = t, cur, 0

        return newhead.next


if __name__ == '__main__':
    t = l1 = ListNode(1)
    t.next = ListNode(2);t=t.next
    t.next = ListNode(3);t=t.next
    t.next = ListNode(4);t=t.next
    t.next = ListNode(5);t=t.next

    ans = Solution().reverseKGroup(l1, 2)
    while ans:
        print ans.val
        ans = ans.next
    
    t = l1 = ListNode(1)
    t.next = ListNode(2);t=t.next
    t.next = ListNode(3);t=t.next
    t.next = ListNode(4);t=t.next
    t.next = ListNode(5);t=t.next

    ans = Solution().reverseKGroup(l1, 3)
    while ans:
        print ans.val
        ans = ans.next

    pass
