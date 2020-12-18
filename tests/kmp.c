#include <string.h>
#include <stdlib.h>

int main()
{
    char S[100];
    char T[100];
    int next[100];
    int s_len, t_len;
    int i = 0;
    int j = 0;
    int flag = 0;

    gets(S);
    gets(T);
    s_len = strlen(S);
    t_len = strlen(T);

    next[0] = -1;
    for (i = 1, j = -1; i < t_len; i = i + 1)
    {
        for (; j >= 0 && T[i] != T[j + 1]; j = next[j])
            ;
        if (T[i] == T[j + 1])
        {
            j = j + 1;
        }
        next[i] = j;
    }

    for (i = 0, j = -1; i < s_len; i = i + 1)
    {
        for (; j >= 0 && S[i] != T[j + 1]; j = next[j])
            ;
        if (S[i] == T[j + 1])
        {
            j = j + 1;
        }
        if (j == t_len - 1)
        {
            printf("%d,", i - j);
            flag = 1;
            j = next[j];
        }
    }
    if (flag == 0)
    {
        printf("No Match\n");
    }
    else{
        printf("\n");
    }

    return 0;
}
