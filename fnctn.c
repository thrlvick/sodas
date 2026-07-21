#include <stdio.h>

int process 
(int var1, int var2 ) {
 return var1 / var2;
}

int multiplier
(int var1, int var2 ) {
 return var1 * var2;
}

int main () {
    int (*ptr)(int , int);
    ptr = &process;

    int result = (*ptr)(5, 5);

    printf("Result: %d\n", result);
    

    ptr = &multiplier;

    result = (*ptr)(7, 8);

    printf("Result: %d\n", result);
    return 0;
}



