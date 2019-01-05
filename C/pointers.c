#include<stdio.h>


int main() {

    int a = 10;
    int *p, *t, **y;

    p = &a;
    t = &(*p);
    y = &p;

    printf("The value of a is %d\n", *p);
    printf("The value of t is %d\n", *t);

    printf("The address of p is %p\n", &p);
    printf("The address of a is %p\n", &a);
    printf("The address of a is %p\n", &(*p));
    printf("The value of y is %p\n", *y);

    return 0;
}
