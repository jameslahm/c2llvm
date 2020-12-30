#include <string.h>
#include <stdlib.h>

int main()
{
    char s[100];
    char t[100];
    int next[100];
    int s_len, t_len;
    int i = 0;
    int j = 0;
    int flag = 0;

    gets(s);
    gets(t);
    s_len = strlen(s);
    t_len = strlen(t);

    next[0] = -1;
    for (i = 1, j = -1; i < t_len; i = i + 1)
    {
        for (; j >= 0 && t[i] != t[j + 1]; j = next[j])
            ;
        if (t[i] == t[j + 1])
        {
            j = j + 1;
        }
        next[i] = j;
    }

    for (i = 0, j = -1; i < s_len; i = i + 1)
    {
        for (; j >= 0 && s[i] != t[j + 1]; j = next[j])
            ;
        if (s[i] == t[j + 1])
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
