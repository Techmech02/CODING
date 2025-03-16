#include<iostream>
using namespace std;
int main()
{
    int num;
    cin>>num;

    int sum=0;
     int i;
        cin>>i;
    do{
        
        sum+=num;
        i--;
    }while(i>0);
    
       cout<<sum<<endl;

       return 0;
}