#include <stdio.h>
void main()
{
    int num,m =1,n=6;
    printf("Print Odd Numbers in a given range m to n:\n");
    for (num = 2; num <= n; num++)
        {
               if (num % 2 == 1)
                  printf ("%d ", num);
         }
}
