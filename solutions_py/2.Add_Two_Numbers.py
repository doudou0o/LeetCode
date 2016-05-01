#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ans_list = ListNode(0)
        p = ans_list
        carry = 0
        while(l1 != None or l2 != None or carry):
            n1 = l1.val if l1 != None else 0
            n2 = l2.val if l2 != None else 0
            cur = n1 + n2 + carry
            if cur > 9:
                cur = cur - 10
                carry = 1
            else:
                carry = 0
            p.next = ListNode(cur)
            p = p.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        return ans_list.next

def build_NodeList(nums):
    newListNode = ListNode(0)
    p = newListNode
    for i in nums:
        p.next = ListNode(i)
        p = p.next
    return newListNode.next

if __name__ == '__main__':
    l1 = build_NodeList([2,4,5])
    l2 = build_NodeList([5,6,4])
    ans = Solution().addTwoNumbers(l1, l2)
    while(ans):
        print ans.val
        ans = ans.next


