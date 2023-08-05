#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define FLAG "W4terCTF{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"

int main() {
    puts("Hello, CTFer!");
    puts("Let me give you the flag...\n");
    sleep(2);

    puts("Hum... I remember the flag is...\n");
    sleep(2);

    puts("But I'm so lazy to type it out...\n");
    sleep(2);

    puts("So I'll just print it out letter by letter...\n");
    sleep(2);

    int len = strlen(FLAG);
    for (int i = 0; i < len; i++) {
        putchar(FLAG[i]);
        fflush(stdout);
        sleep(2 << (i / 2 + i % 2));
    }

    return 0;
}
