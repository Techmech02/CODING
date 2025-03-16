#include<iostream>
using namespace std;
int main()
{
int a,b;
cout<<"ENTER TWO INTEGERS:  "<<endl;
cout<<"a"<<endl;
cin>>a;
cout<<"b: "<<endl;
cin>>b; 

cout<<"""ENTER YOUR OPERATION(+,-,*,/,%):  "<<endl;
char c;
cin>>c;
switch(c){
case '+':
cout<<"SUM OF GIVEN INTEGERS:"<<a+b<<endl;
    break;
case'-':
cout<<"DIFFRENCE OF GIVEN INTEGERS:"<<a-b<<endl;
    break;
case'*':
cout<<"MULTIPLICATION OF GIVEN INTEGERS:"<<a*b<<endl;
    break;
case'/':
cout<<"DIVISION OF GIVEN INTEGERS:"<<a/b<<endl;
    break;
case'%':
cout<<"REMAINDER OF GIVEN INTEGERS:"<<a%b<<endl;
    break;
default:     cout<<"NO GIVEN OPERATOR USED"<<endl;
    break;
}
return 0;
}