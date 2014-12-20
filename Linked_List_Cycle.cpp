/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL)return false;
        if(head->next==NULL)return false;
        ListNode *fast=head;
        ListNode *slow=head;
        while(true){
            fast=fast->next->next;
            slow=slow->next;
			if(fast == NULL || fast->next==NULL)return false;
			if(fast==slow)return true;
        }
    }
};