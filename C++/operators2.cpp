#include<iostream>
using namespace std;
int main(){
    bool exp1;
    cout<<"ENTER EXPRESSION 1:    "<<endl;
    cin>>exp1;
    bool exp2;
    cout<<"enter expression 2:    "<<endl;
    cin>>exp2;
    
    cout<<(exp1&&exp2)<<endl;
    cout<<(exp1||exp2)<<endl;
    cout<<(!exp1)<<endl;

    
   
    return 0;
}