#include<iostream>
using namespace std;
int main(){
    int num1,num2;
    cout<<"ENTER TWO INTEGERS:-->"<<endl<<"a:"<<endl;
    cin>>num1;
    cout<<"b:"<<endl;
    cin>>num2;

    char c;
    cout<<"ENTER GIVEN OPERATOR TO BE USED(+,-,/,%):"<<endl;
    cin>>c;

    switch (c){
        case'+':
    cout<<"SUM OF GIVEN OPERATON IS:"<<num1+num2<<endl;
        break;

        case'-':
    cout<<"DIFFRENCE OF GIVEN OPERATON IS:"<<num1-num2<<endl;
        break;

        case'*':
    cout<<"MULTIPLICATION OF GIVEN OPERATON IS:"<<num1*num2<<endl;
        break;

        case'/':
    cout<<"DIVISION OF GIVEN OPERATON IS:"<<num1/num2<<endl;
        break;

        default:
    cout<<"REMAINDER OF GIVEN OPERATON IS:"<<num1%num2<<endl;
        break;
        
    }
    return 0;

}