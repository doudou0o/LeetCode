#include <iostream>
#include <stdlib.h>
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
using namespace std;
ListNode* removeNode(ListNode* head,ListNode* p,ListNode* pre)
{
    if ( pre == NULL) return head->next;
    pre->next = p->next;
    p->next = NULL;
    free(p);
    return head;
}
ListNode* removeNthFromEnd(ListNode* head,int n)
{
    ListNode* p1 = head;
    if ( n==0 )return head ;
    while(n--){
        if ( p1 == NULL ) return head;
        p1 = p1->next;
    }
    ListNode* p2 = head;
    ListNode* p2_pre = NULL;
    while(p1 != NULL){
        p2_pre = p2;
        p2 = p2->next;
        p1 = p1->next;
    }
    return removeNode(head,p2,p2_pre);
}
void print(ListNode* head)
{
    while(head!=NULL){
        std::cout << head->val;
        head = head->next;
    }
    std::cout << std::endl;
}
int main(int argc, const char *argv[])
{
    ListNode* head = (ListNode*)malloc(sizeof(ListNode));
    ListNode* n1 = (ListNode*)malloc(sizeof(ListNode));
    ListNode* n2 = (ListNode*)malloc(sizeof(ListNode));
    ListNode* n3 = (ListNode*)malloc(sizeof(ListNode));
    head->val = 1;
    n1->val = 2;
    n2->val = 3;
    n3->val = 4;
    head->next = n1;
    n1->next = n2;
    n2->next = n3;
    n3->next = NULL;
    ListNode* ans = removeNthFromEnd(head,0);
    print(ans);
    return 0;
}
