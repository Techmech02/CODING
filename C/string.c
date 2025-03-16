#include<stdio.h>
#include<conio.h>
/// @brief 
/// @param  
int main(void)
{
    int i;
    char s[15];
    printf("enter a string");
    for(i=0;i<5;i++)
    {
        scanf("%c",&s[i]);
    }
    for(i=0;i<5;i++)
    {
        printf("%c",s[i]);
    }
    
}