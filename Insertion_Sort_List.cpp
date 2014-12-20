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
    ListNode *insertionSortList(ListNode *head) {
        ListNode *ans=NULL;
    	ListNode *cur,*pre;
    	bool find;
    	while(head != NULL){
    		if(ans == NULL){ans=head;head=head->next;ans->next=NULL;continue;}
    		if(head->val < ans->val){
    			ListNode *t=head;
    			head = head->next;
    			t->next=ans;
    			ans=t;
    			continue;
    		}
    		cur=ans->next;pre=ans;
    		find = false;
    		while(!( find || cur == NULL)){
    			if(head->val < cur->val){find=true;continue;}
    			pre=cur;
    			cur=cur->next;
    		}
    		ListNode *t=head;
    		head = head->next;
    		pre->next = t;
    		t->next=cur;
    	}
    
    	return ans;
    }
};