#include<iostream>
using namespace std;

int main()
{
    int a,b;
    cout<<"ENTER TWO INTEGERS:    "<<endl<<"a: "<<endl;
    cin>>a;

    cout<<"b: "<<endl;
    cin>>b;

    char c;
    cout<<"ENTER A OPERATOR(+,-,*,/,%):   "<<endl;
    cin>>c;

    switch (c)
    {
    case '+':
        cout<<"SUM: "<<a+b<<endl;
        break;
    
    case '-':
        cout<<"SUBSTRACTION: "<<a-b<<endl;
        break;

        case '*':
        cout<<"MULTIPLE: "<<a*b<<endl;
        break;

        case '/':
        cout<<"DIVISION: "<<a/b<<endl;
        break;

        case '%':
        cout<<"REMAINDER: "<<a%b<<endl;
        break;

    default:  cout<<"INPUT ERROR DECTECTED"<<endl;
        break;
    }
    return 0;
}