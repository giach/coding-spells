#include<iostream>
#include<stdio.h>
#include<stdlib.h>

#define N 10

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    
    ListNode(int x) : val(x), next(NULL) {}
    
    void printList() {
        ListNode *tmp = this;
        while(tmp) {
            cout << tmp->val << " ";
            tmp = tmp->next;
        }

        cout << endl;
    }
    
};

class Solution {
public:
    ListNode* merge2Lists(ListNode* l1, ListNode l2) {
        return NULL;
    }
};
int main() {
    
    int i;
    ListNode *head1, *head2;
    ListNode *tmp, *p1, *p2;

    head1 = new ListNode(0);
    head2 = new ListNode(1);

    tmp = head1;
    
    for(i = 2; i < N; i += 2) {
        tmp->next = new ListNode(i);
        tmp = tmp->next;
    }

    tmp = head2;
    for(i = 3; i < N; i += 2) {
        tmp->next = new ListNode(i);
        tmp = tmp->next;
    }

    int tv;
    while(p1 && p2) {
        if(p1->val < p2->val) {
            p1 = p1->next;
        }
        tv = p1->val;
        p1->val = p2->val;
        
    }

    head1->printList();
    head2->printList();

    return 0;
}
