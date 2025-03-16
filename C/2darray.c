#include<stdio.h>
#include<conio.h>

int main(void)
{
    int a[100][100];
    int m,n,i,j,p,q;
    printf("enter row and coloumn: ");
    scanf("%d,%d",&m,&n);
    printf("ENTER ELEMNTS INTO THE ARRAY:  ");
    for ( i = 0; i < m; i++)
    {  
        for ( j = 0; j <n; j++)
        {
            scanf("%d",&a[i][j]);
            printf("\n");
        }  
    }
    printf("the elements are:   ");
      for ( i = 0; i < m; i++)
    {  
        for ( j = 0; j <n; j++)
        {
            printf("%d",a[i][j]);
        }  printf("\n");
    }

}