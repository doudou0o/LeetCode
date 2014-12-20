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
    ListNode *sortList(ListNode *Head) {
        if(Head == NULL || Head->next == NULL)return Head;

    	ListNode *fast;
    	ListNode *slow,*pre;
    	fast=Head;slow=Head;
    	while(fast != NULL && fast->next != NULL ){
    		fast = fast->next->next;
    		pre=slow;
    		slow = slow->next;
    	}
    	pre->next=NULL;
    	ListNode* left=sortList(Head);
    	ListNode* right=sortList(slow);
    	return merge(left,right);
    }
    ListNode* merge(ListNode *a , ListNode *b){
    	if( a==NULL )return b;
    	if( b==NULL )return a;
    	
    	ListNode *ans=NULL;
    	ListNode *end_ans=NULL;
    	
    	while(a != NULL && b!=NULL){
    		if ( a->val <= b->val ){
    			if(ans == NULL){
    				ans=a;
    				end_ans=a;
    			}
    			else{
    				end_ans->next = a;
    				end_ans=end_ans->next;
    			}
    			a=a->next;
    		}
    		else{
    			if(ans == NULL){
    				ans=b;
    				end_ans=b;
    			}
    			else{
    				end_ans->next = b;
    				end_ans=end_ans->next;
    			}
    			b=b->next;
    		}
    	}
    	if(a == NULL){end_ans->next=b;}
    	if(b == NULL){end_ans->next=a;}

    	return ans;
    }
};