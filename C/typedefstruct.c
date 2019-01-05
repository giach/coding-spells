#include<stdio.h>
#include<stdlib.h>

typedef struct {

    int value;
    struct Node *next;

} Node;

int main() {
    
    Node dummy;
    dummy.value = 10;
    dummy.next = NULL;

    printf("The value is %d\n", dummy.value);

    return 0;
}
