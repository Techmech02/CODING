#include<iostream>
using namespace std;
int main()
{
    int num,i,sum=0;
    cin>>num;
    cin>>i;
    do{
    sum+=i;
    num--;
    }while ( num > i );

    cout<<sum<<endl;

    return 0;
}