#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>

char word[0x101];

void menu() {
    printf("1. Add word\n");
    printf("2. Search word\n");
    printf("3. Edit word\n");
    printf("4. Delete word\n");
    printf("Enter your choice: ");
}

struct Node {
    uint8_t ref;
    struct Node* next[26];
    char* description;
};
typedef struct Node Node;

int read_word() {
    int len;
    printf("Enter word length: ");
    scanf("%d", &len);
    if(len > 0x100) {
        printf("Too long!\n");
        return 0;
    }
    if(len <= 0) {
        printf("Too short!\n");
        return 0;
    }
    printf("Enter word: ");
    int r = read(0, word, len);
    // clean the last \n character and update the length
    if(word[r - 1] == '\n') {
        word[r - 1] = 0;
        r--;
    }
    return r;
}

void init_node(struct Node* n) {
    n->description = NULL;
    n->ref = 1;
    for(int i = 0; i < 26; i++) {
        n->next[i] = NULL;
    }
}

uint8_t validate_word(char* str) {
    for(int i = 0; i < strlen(str); i++) {
        if(str[i] < 'a' || str[i] > 'z') {
            // word must be lower case and only contain a-z
            printf("Invalid word! Word must be lower case and only contain a-z\n");
            return 0;
        }
    }
    return 1;
}

void release(Node* n) {
    n->ref--;
    if(n->ref == 0) {
        if(n->description) free(n->description);
        for(int i = 0; i < 26; i++) {
            if(n->next[i]) release(n->next[i]);
        }
        free(n);
    }
}

void add(Node* root) {
    int len;
    int wl = read_word();

    // to lower case
    for(int i = 0; i < wl; i++) {
        if(word[i] >= 'A' && word[i] <= 'Z') {
            word[i] = word[i] - 'A' + 'a';
        }
    }
    if(!validate_word(word)) return;
    Node* cur = root;
    for(int i = 0; i < wl; i++) {
        if(cur->next[word[i] - 'a'] == NULL) {
            cur->next[word[i] - 'a'] = malloc(sizeof(Node));
            init_node(cur->next[word[i] - 'a']);
        }
        cur->next[word[i] - 'a']->ref++;
        cur = cur->next[word[i] - 'a'];
    }
    cur->description = NULL;
    cur->ref--;
    printf("Enter description length: ");
    scanf("%d", &len);
    cur->description = (char*)malloc(len + 1);
    printf("Enter description: ");
    read(0, cur->description, len);
}

void search(Node* root) {
    int len;
    int wl = read_word();

    // to lower case
    for(int i = 0; i < wl; i++) {
        if(word[i] >= 'A' && word[i] <= 'Z') {
            word[i] = word[i] - 'A' + 'a';
        }
    }
    if(!validate_word(word)) return;
    Node* cur = root;
    for(int i = 0; i < wl; i++) {
        if(cur->next[word[i] - 'a'] == NULL) {
            printf("Not found\n");
            return;
        }
        cur = cur->next[word[i] - 'a'];
    }
    printf("Found\n");
    printf("Description: %s\n", cur->description);
}

void edit_word(Node* root) {
    int len;
    int wl = read_word();

    // to lower case
    for(int i = 0; i < wl; i++) {
        if(word[i] >= 'A' && word[i] <= 'Z') {
            word[i] = word[i] - 'A' + 'a';
        }
    }
    if(!validate_word(word)) return;
    Node* cur = root;
    for(int i = 0; i < wl; i++) {
        if(cur->next[word[i] - 'a'] == NULL) {
            printf("Not found\n");
            return;
        }
        cur = cur->next[word[i] - 'a'];
    }
    if(cur->description) free(cur->description);
    printf("Enter description length: ");
    scanf("%d", &len);
    cur->description = (char*)malloc(len + 1);
    printf("Enter description: ");
    read(0, cur->description, len);
}

void delete_word(Node* root) {
    int len;
    int wl = read_word();

    // to lower case
    for(int i = 0; i < wl; i++) {
        if(word[i] >= 'A' && word[i] <= 'Z') {
            word[i] = word[i] - 'A' + 'a';
        }
    }
    if(!validate_word(word)) return;
    Node* cur = root;
    for(int i = 0; i < wl; i++) {
        if(cur->next[word[i] - 'a'] == NULL) {
            printf("Not found\n");
            return;
        }
        cur = cur->next[word[i] - 'a'];
    }
    void traverse(Node * root, int maxlen, char* word, int depth);
    traverse(root, wl, word, 0);
}

void traverse(Node* root, int maxlen, char* word, int depth) {
    Node* cur = root;
    if(depth == maxlen - 1) {
        if(cur->next[word[depth] - 'a']->description != NULL) {
            free(cur->next[word[depth] - 'a']->description);
        }
        free(cur->next[word[depth] - 'a']);
        cur->next[word[depth] - 'a'] = NULL;
        return;
    }
    Node* n = cur->next[word[depth] - 'a'];
    n->ref--;
    traverse(n, maxlen, word, depth + 1);
    if(n->ref == 0) {
        if(n->description) free(n->description);
        free(n);
    }
}

void init() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
}

Node* root;
int main() {
    init();
    int choice;
    root = malloc(sizeof(struct Node));
    init_node(root);
    while(1) {
        menu();
        scanf("%d", &choice);
        switch(choice)
        {
            case 1:
                add(root);
                break;
            case 2:
                search(root);
                break;
            case 3:
                edit_word(root);
                break;
            case 4:
                delete_word(root);
                break;
            default:
                break;
        }
    }
}
