#include<iostream>
using namespace std;

int main()
{
    int a=0;
    while (a<19991)
    {
      if (a%2!=0)
      {
        cout<<a<<endl;
       
      }else{
            cout<<'-'<<endl;
            }
            a++;
    }
    return 0;

}