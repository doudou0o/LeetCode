/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
    	struct RandomListNode* ans =NULL;
    	struct RandomListNode* t=head;
    	struct RandomListNode* temp=NULL;
    	struct RandomListNode* cur=NULL;
    	map<RandomListNode*,RandomListNode*>hm;
    
    	if(t==NULL)return NULL;
    	else{
    		temp=(RandomListNode*)malloc(sizeof(RandomListNode));
    		temp->next=NULL;temp->random=NULL;
    		temp->label=t->label;
    		ans = temp;
    		cur = ans;		
    		hm.insert(make_pair(t,ans));
    		t=t->next;
    	}
    
    	while(t != NULL){
    		temp=(RandomListNode*)malloc(sizeof(RandomListNode));
    		temp->next=NULL;temp->random=NULL;
    		temp->label=t->label;
    		cur->next = temp;
    		cur=cur->next;
    		hm.insert(make_pair(t,cur));
    		t=t->next;
    	}
    
    	t=head;
    	cur=ans;
    	while(t!=NULL){
    		temp=t->random;
    		cur->random=hm[temp];
    		t=t->next;
    		cur=cur->next;
    	}
    	return ans;
    }
};