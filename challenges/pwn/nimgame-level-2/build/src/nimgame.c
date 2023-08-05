#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <stdint.h>

int player_select(int tokens_cnt, int take);
int computer_select(int tokens_cnt);
void success();

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    srand(time(NULL));
    printf("W4terCTF Nim Game level 2\n");
    printf("How to play: There are 16 tokens on the table. Each player can take 1, 2, or 3 tokens at a time. The player who takes the last token wins.\n\n");

    char input[32];

    int tokens_cnt = 16;

    printf("There are %i tokens on the table.\n", tokens_cnt);
    while(tokens_cnt > 0) {
        printf("How many tokens would you like to take?: ");
        read(0, input, 0x320);
        printf("\nPlayer takes %s tokens.\n", input);
        input[8] = 0;
        int token = atoi(input);

        int next_tokens_cnt = player_select(tokens_cnt, token);

        if(next_tokens_cnt == tokens_cnt) {
            continue;
        }

        tokens_cnt = next_tokens_cnt;
        if(tokens_cnt == 0) {
            printf("Player wins.");
            success();
            break;
        }

        tokens_cnt = computer_select(tokens_cnt);
        if(tokens_cnt == 0) {
            printf("Computer wins.");
            break;
        }
    }

    return 0;
}

void success() {
    printf("Don't be too greedy! I have already given you a flag in level 0\n");
}

int player_select(int tokens_cnt, int take) {
    if(take < 1 || take > 3) {
        printf("Number of tokens must be between 1 and 3.\n\n");
        return tokens_cnt;
    }

    int remaining_tokens_cnt = tokens_cnt - take;

    printf("%i tokens remaining.\n\n", remaining_tokens_cnt);

    return remaining_tokens_cnt;
}

uint32_t smart_decide() {
    uint32_t take = rand() % 4;
    return take;
}

int computer_select(int tokens_cnt) {
    int take = tokens_cnt % 4;
    if(take == 4) {
        take = 1;
    }

    int remaining_tokens_cnt = tokens_cnt - take;

    printf("\nComputer takes %i tokens.\n", take);
    printf("%i tokens remaining.\n\n", remaining_tokens_cnt);

    return remaining_tokens_cnt;
}
