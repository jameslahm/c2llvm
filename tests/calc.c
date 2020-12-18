#include <stdio.h>
#include <string.h>

int main()
{
    char expr[100];
    int nums[100];
    char ops[100];

    int nums_index = -1;
    int ops_index = -1;

    gets(expr);
    int len = strlen(expr);
    int i;
    for (i = len - 1; i >= 0; i = i - 1)
    {
        expr[i + 1] = expr[i];
    }
    expr[0] = '(';
    expr[len + 1] = ')';
    len = len + 2;

    i = len - 1;
    int num = 0;
    int k = 1;
    while (i >= 0)
    {
        if (expr[i] == '*')
        {
            ops_index = ops_index + 1;
            ops[ops_index] = '*';
            i = i - 1;
        }
        else if (expr[i] == '/')
        {
            ops_index = ops_index + 1;
            ops[ops_index] = '/';
            i = i - 1;
        }
        else if (expr[i] == '+')
        {
            while (ops_index >= 0 && ((ops[ops_index] == '*') || (ops[ops_index] == '/')))
            {
                if (ops[ops_index] == '*')
                {
                    nums[nums_index - 1] = nums[nums_index] * nums[nums_index - 1];
                }
                else
                {
                    nums[nums_index - 1] = nums[nums_index] / nums[nums_index - 1];
                }
                nums_index = nums_index - 1;
                ops_index = ops_index - 1;
            }
            ops_index = ops_index + 1;
            ops[ops_index] = '+';
            i = i - 1;
        }
        else if (expr[i] == '-')
        {
            while (ops_index >= 0 && ((ops[ops_index] == '*') || (ops[ops_index] == '/')))
            {
                if (ops[ops_index] == '*')
                {
                    nums[nums_index - 1] = nums[nums_index] * nums[nums_index - 1];
                }
                else
                {
                    nums[nums_index - 1] = nums[nums_index] / nums[nums_index - 1];
                }
                nums_index = nums_index - 1;
                ops_index = ops_index - 1;
            }
            ops_index = ops_index + 1;
            ops[ops_index] = '-';
            i = i - 1;
        }
        else if (expr[i] == '(')
        {
            while (ops[ops_index] != ')')
            {
                char ch = ops[ops_index];
                ops_index = ops_index - 1;
                if (ch == '+')
                {
                    nums[nums_index - 1] = nums[nums_index] + nums[nums_index - 1];
                }
                else if (ch == '-')
                {
                    nums[nums_index - 1] = nums[nums_index] - nums[nums_index - 1];
                }
                else if (ch == '*')
                {
                    nums[nums_index - 1] = nums[nums_index] * nums[nums_index - 1];
                }
                else if (ch == '/')
                {
                    nums[nums_index - 1] = nums[nums_index] / nums[nums_index - 1];
                }
                nums_index = nums_index - 1;
            }
            ops_index = ops_index - 1;
            i = i - 1;
        }
        else if (expr[i] == ')')
        {
            ops_index = ops_index + 1;
            ops[ops_index] = ')';
            i = i - 1;
        }
        else
        {
            num = 0;
            k = 1;
            while (i >= 0 && expr[i] >= '0' && expr[i] <= '9')
            {
                num = num + (expr[i] - '0') * k;
                k = k * 10;
                i = i - 1;
            }
            nums_index = nums_index + 1;
            nums[nums_index] = num;
        }
    }
    printf("%d\n", nums[0]);
    return 0;
}
