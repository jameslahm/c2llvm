#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main()
{
    char s[100];
    int n[100];
    int num = 0;
    gets(s);

    int i = 0;
    int j = 0;
    int len = strlen(s);
    for (i = 0; i < len; i = i + 1)
    {
        if (s[i] != ',')
        {
            int tmp = s[i];
            n[j] = tmp - 48;
            j = j + 1;
            num = num + 1;
        }
    }

    for (i = 0; i < num; i = i + 1)
    {
        for (j = 0; j < num - i - 1; j = j + 1)
        {
            if (n[j] > n[j + 1])
            {
                int tmp = n[j];
                n[j] = n[j + 1];
                n[j + 1] = tmp;
            }
        }
    }

    for (i = 0; i < num-1; i = i + 1)
    {
        printf("%d,", n[i]);
    }
    printf("%d\n",n[num-1]);

    return 0;
}