#include<stdio.h>
#include<iostream>

using namespace std;

class LinkedList {
    
    class Node {
    public:
        int val;
        Node *next;

        Node(int v): val(v), next(NULL) {}

    };
public:
    Node *head;
    Node *end;

    LinkedList(): head(NULL) {}

public:
    void append(int val)
    {
        if (head == NULL) {
            head = new Node(val);
            end = head;
        }
        else {
            end->next = new Node(val);
            end = end->next;
        }
    }

    void print()
    {
        Node *tmp = head;

        while(tmp != NULL) {
            cout << tmp->val << " ";
            tmp = tmp->next;
        }

        cout << endl;
    }
    
};


int main() {

    LinkedList *list;

    list = new LinkedList();

    list->append(10);
    list->print();

    list->append(20);
    list->append(30);
    list->append(40);
    list->append(50);
    list->print();

    return 0;
}
