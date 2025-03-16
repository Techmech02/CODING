#include<stdio.h>
#include<string.h>
#include<conio.h>
void display(char*,char*,int);
main()
{
    {
        char name[25];
        char author[25];
        int callno;

    };
    struct book b1={"Let us c","YPK","101"};
    display(b1);
}
void display(struct book)
{
    pf("%s%s%d", s.name,s.author,s.callno);
}