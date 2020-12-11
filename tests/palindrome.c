#include <string.h>
#include <stdlib.h>

int main()
{
	char s[100];
	int i = 0;
	int len = 0;
	int flag = 0;
	gets(s);
	len = strlen(s);
	for (i = 0; i + i < len && flag == 0; i = i + 1)
	{
		if (s[i] != s[len - 1 - i])
		{
			printf("False\n");
			flag = 1;
		}
	}
	if (flag == 0)
	{
		printf("True\n");
	}
	return 0;
}