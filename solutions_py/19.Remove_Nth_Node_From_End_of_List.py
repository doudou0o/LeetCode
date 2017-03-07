#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head

        i,j = newHead, newHead

        while n > 0:
            n = n - 1
            if j.next == None:
                return head
            else:
                j = j.next

        while j.next != None:
            i = i.next
            j = j.next

        i.next = i.next.next

        return newHead.next


if __name__ == '__main__':
    #1
    head = ListNode(1)
    f = head
    f.next = ListNode(2); f=f.next;
    f.next = ListNode(3); f=f.next;
    f.next = ListNode(4); f=f.next;
    f.next = ListNode(5); f=f.next;

    ans = Solution().removeNthFromEnd(head, 2)
    while ans!=None:
        print ans.val
        ans = ans.next

    #2
    head = ListNode(1)
    ans = Solution().removeNthFromEnd(head, 1)
    print ans

    #3
    head = ListNode(1)
    f = head
    f.next = ListNode(2); f=f.next;
    f.next = ListNode(3); f=f.next;
    ans = Solution().removeNthFromEnd(head, 3)
    while ans!=None:
        print ans.val
        ans = ans.next

