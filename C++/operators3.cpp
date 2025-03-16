#include<iostream>
using namespace std;
int main(){
    int num1=5;
    cout<<(num1<<1)<<endl;
    cout<<(num1>>1)<<endl;
    
    int num2=8;
    cout<<(num2<<2)<<endl;
    cout<<(num2>>3)<<endl;
  
    cout<<(num1|num2)<<endl;
    cout<<(num1&num2)<<endl;
    cout<<(num1^num2)<<endl;


    int a=6;
    cout<<(a++)<<endl;

    int b=6;
    cout<<(++b)<<endl;


    return 0;
}