#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h> // Required for dlsym

int puts(const char *str) {
    // This is our hijacked version
    printf("[!] Hooked! You tried to print: %s\n", str);
    return 0;
}