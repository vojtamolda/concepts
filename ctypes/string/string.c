#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* c_string_alloc(void) {
    char* ptr = strdup("I am a string from C!");
    printf("C allocate %p: '%s'\n", ptr, ptr);
    return ptr;
}

void c_string_modify(char *ptr) {
    printf("C modify %p: '%s'\n", ptr, ptr);
    for (int i = 0; i < strlen(ptr); i++) ptr[i]++;
}

void c_string_print(char* ptr) {
    printf("C print %p: '%s'\n", ptr, ptr);
}

void c_string_free(char* ptr) {
    printf("C free %p: '%s'\n", ptr, ptr);
    free(ptr);
}
