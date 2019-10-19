#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void win() {
    char *params[] = {"/bin/sh", NULL};
    execv("/bin/sh", params);
    return;
}

int main() {
    char buf[10];
    
    printf("Enter\n");
    gets(buf);
    printf("You entered: %s\n", buf);
    return 0;
}