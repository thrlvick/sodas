#include <stdio.h>
#include <stdatomic.h>

int main() {
    atomic_int my_atomic_var = 0;
    atomic_store(&my_atomic_var, 10);
    int current_val = atomic_load(&my_atomic_var);
    printf("the value is: %d\n", current_val);
    return 0;
}

