#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    scanf("%i", &x);
    x = (((~(x-1)) & x)- 1);
    printf("%i", x);
    return 0;
}
