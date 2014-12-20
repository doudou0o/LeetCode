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
    ListNode *detectCycle(ListNode *head) {
        if(head==NULL)return NULL;
        if(head->next==NULL)return NULL;
        ListNode *fast=head;
        ListNode *slow=head;
        while(true){
            fast=fast->next->next;
            slow=slow->next;
			if(fast == NULL || fast->next==NULL)return NULL;
			if(fast==slow)break;
        }
		slow=head;
		while(true){
			if(fast==slow)return slow;
			slow=slow->next;
			fast=fast->next;
		}
    }
};