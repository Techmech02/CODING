#include<iostream>
using namespace std;

int main()
{
    int a;
    cin>>a;

    if((a%7 ==0) || (a%3 ==0))
    {
        cout<<"OKAY"<<endl;

    }
    else{
        cout<<"NOT OKAY "<<endl;
    }

    return 0;
}
