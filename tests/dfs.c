#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int value;
    int left;
    int right;
};

struct Node nodes[100];

int num;

void pre_order(int n)
{
    if (n >= num)
    {
        return;
    }

    printf("%d ", nodes[n].value);
    if (nodes[n].left != -1)
    {
        pre_order(nodes[n].left);
    }
    if (nodes[n].right != -1)
    {
        pre_order(nodes[n].right);
    }

    return;
}

int main()
{
    char s[100];
    gets(s);

    int i = 0;
    int j = 0;
    int len = strlen(s);
    for (i = 0; i < len; i = i + 1)
    {
        if (s[i] != ',')
        {
            int tmp = s[i];

            nodes[j].value = tmp - 48;
            nodes[j].left = -1;
            nodes[j].right = -1;

            j = j + 1;
            num = num + 1;
        }
    }

    for (i = 0; i < num; i = i + 1)
    {
        if (2 * i + 1 < num)
        {
            nodes[i].left = 2 * i + 1;
        }
        if (2 * i + 2 < num)
        {
            nodes[i].right = 2 * i + 2;
        }
    }

    pre_order(0);
    printf("\n");

    return 0;
}