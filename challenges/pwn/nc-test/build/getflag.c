#include <stdio.h>
#include <stdlib.h>

int main()
{
    char* flag = getenv("GZCTF_FLAG");
    if(flag == NULL) {
        printf("flag{this_is_a_static_flag}\n");
        return 0;
    }
    printf("%s\n", flag);
    return 0;
}
