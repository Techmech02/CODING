#include<stdio.h>
#include<conio.h>
#include<string.h>

int main (void)
{
    char s[100];
    printf("Before:");
    scanf("%s",&s);
    printf("after:");
    for(int i=0;i< strlen(s);i++)
    {
        if( s[i] >= 'a' && s[i]<= 'z')
        {
            printf("%c",s[i]-32);
        }
          else
        {
            printf("%c",s[i]);

        }
    }printf("\n");
}