#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function 
    int *res1, *res2;

    (*res1) = (*a) + (*b);
    (*res2) = ((*a)>(*b)? (*a)-(*b):(*b)-(*a));
    (*a) = (*res1);
    (*b) = (*res2);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

