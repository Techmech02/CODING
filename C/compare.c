#include<cs50.h>
#include<stdio.h>

int main(void)
{
    int a = get_int("ENTER NUMBER 1  \n");
    int b = get_int("ENTER NUMBER 2  \n");

    if(a<b)
    {
        printf("a is smaller than b\n");
    }else{
        printf("a is larger than b\n");
    }
}