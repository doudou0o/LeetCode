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
    void reorderList(ListNode *head) {
        ListNode *fast=head;
    	ListNode *slow=head;
    	ListNode *pre=NULL;
    	while(!(fast==NULL || fast->next == NULL)){
    		fast=fast->next->next;
    		pre=slow;
    		slow=slow->next;
    	}
    	if(fast == slow)return;
    	pre->next=NULL;//¶ÏÁ´
    	//·´×ªslow
    	ListNode *head2=slow;
    	slow=slow->next;
    	head2->next=NULL;
    	while(slow!=NULL){
    		ListNode *t=slow->next;
    		slow->next=head2;
    		head2=slow;
    		slow=t;
    	}
    	//Æ´½Ó
    	ListNode* cur=head;
    	ListNode* head1=head->next;
    	cur->next=NULL;
    	while(head1!=NULL){
    		cur->next=head2;
    		cur=cur->next;
    		if(head2!=NULL)
    			head2=head2->next;
    
    		cur->next=head1;
    		cur=cur->next;
    		if(head1!=NULL)
    			head1=head1->next;
    	}
    	cur->next=head2;
    }
};s