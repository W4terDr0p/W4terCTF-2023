#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int a[3][3];
void success() { system("/bin/sh"); }
void vulnerable()
{
    char s[12];
    //   fflush(stdin);
    puts("You win!!! Tell me your name:");
    // fgets(s, 1000, stdin);
    gets(s);
    puts("soooooooo cool!");
    return;
}
void init() {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    alarm(60);
}

void outputBoard()
{
    puts("--------current chessBoard---------");
    int i, j;
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
        {
            if (j == 0)
                printf("|");
            if (a[i][j] == 1)
                printf("x");
            if (a[i][j] == 2)
                printf("o");
            if (a[i][j] == 0)
                printf(" ");
            printf("|");
            if (j == 2)
                printf("\n");
        }
    puts("Let's go!!");
}

int checkBoard()
{
    int i, j;
    for (i = 0; i < 3; i++)
    {
        if (a[i][0] != 0 && a[i][0] == a[i][1] && a[i][0] == a[i][2])
        {
            return a[i][0];
        }
        if (a[0][i] != 0 && a[0][i] == a[1][i] && a[0][i] == a[2][i])
        {
            return a[0][i];
        }
    }
    if (a[0][0] != 0 && a[0][0] == a[1][1] && a[1][1] == a[2][2])
    {
        return a[1][1];
    }
    if (a[0][2] != 0 && a[0][2] == a[1][1] && a[1][1] == a[2][0])
    {
        return a[1][1];
    }
    return 0;
}

bool play()
{
    init();
    srand(time(0));
    int rest = 9;
    memset(a, 0, sizeof a);
    bool isNPC = false;
    while (rest > 0)
    {
        outputBoard();
        if (isNPC)
        {
            puts("My turn!");
            int p = rand() % 3;
            if (p)
            {
                puts("ooops, I suddenly fall asleep.......");
                isNPC ^= 1;
            }
            else
            {
                isNPC ^= 1;
                p = rand() % rest;
                int i, j;
                for (i = 0; i < 3 && p > 0; i++)
                    for (j = 0; j < 3 && p > 0; j++)
                        if (a[i][j] == 0)
                        {
                            --p;
                            if (p == 0)
                            {
                                a[i][j] = 2;
                                printf("I play at (%d, %d)\n", i, j);
                                rest--;
                                break;
                            }
                        }
            }
        }
        else
        {
            puts("Your turn!");
            puts("Please give me a position(0-8):");
            int pos = 0;
            scanf("%d", &pos);
            getchar();
            if (pos < 9 && pos >= 0 && a[pos / 3][pos % 3] == 0)
            {
                a[pos / 3][pos % 3] = 1;
                rest--;
                printf("You play at: (%d, %d)\n", pos / 3, pos % 3);
            }
            else
            {
                int i, j, p;
                for (i = 0, p = 0; i < 3 && p == 0; i++)
                    for (j = 0; j < 3; j++)
                        if (a[i][j] == 0)
                        {
                            a[i][j] = 1;
                            p = 1;
                            rest--;
                            printf("Wrong Position! I help you play at: (%d, %d)\n", i, j);
                            break;
                        }
            }
            isNPC ^= 1;
        }
        int tmp = checkBoard();
        if (tmp == 0)
        {
            continue;
        }
        if (tmp == 2)
        {
            return false;
        }
        if (tmp == 1)
        {
            return true;
        }
    }
    return false;
}
int main(int argc, char **argv)
{
    puts("Welcome to ez Tic-Tac-Toe!");
    if (!play())
    {
        puts("you loose! Try again!");
        return 0;
    }
    vulnerable();
    return 0;
}