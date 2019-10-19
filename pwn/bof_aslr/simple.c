#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    char buf[0x10][0x8];
    int choice, i, ctr;
    char c;

    memset(buf, '\0', 0x10*0x8);
    while (1) {
        printf("Choice\n");
        scanf("%d", &choice);
        if (choice < 0)
            break;
        printf("0x");
        char *x = buf[choice];
        for (int i = 7; i >= 0 ; i--)
            printf("%02x", (unsigned char)*(x+i));
        printf("\n");

        ctr = 0;
        while ((i = read(0, &c, 1)) > 0 && c != '\n')
            buf[choice][ctr++] = c;
    }
    return 0;
}