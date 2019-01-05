#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<vector>
#include<stack>

using namespace std;

typedef struct Node {
    int value;
    Node *left;
    Node *right;

    Node(int value) {
        this->value = value;
        this->left =  NULL;
        this->right = NULL;
    }
} Node;

void insert(Node *root, Node *t) {

    if (root == NULL)
        root = t;

    if(t->value < root->value) {
        if(root->left != NULL) {
            insert(root->left, t);
        }
        else {
            root->left = t;
        }
    }
    else {
        if(root->right != NULL) {
            insert(root->right, t);
        }
        else {
            root->right = t;
        }
    }
}



void preorder(Node *root) {
    cout << root->value << " ";

    if (root->left != NULL) {
        preorder(root->left);
    }
    if(root->right != NULL) {
        preorder(root->right);
    }
}

void inorder_stack(Node *root) {
    stack<Node*> s;
    vector<int> result;
    
    Node *curr = root;

    while(curr != NULL || !s.empty()) {
        while(curr != NULL) {
            s.push(curr);
            curr = curr->left;
        }
        curr = s.top();
        s.pop();
        result.push_back(curr->value);
        curr = curr->right;

    }

    for(int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }

    cout << endl;
}

int main() {

    Node *root = new Node(7);
    Node *t;

    t = new Node(5);
    insert(root, t);

    t = new Node(10);
    insert(root, t);
   
    t = new Node(20);
    insert(root, t);

    

    cout << endl;
    return 0;
}
