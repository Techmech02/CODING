#include<iostream>
using namespace std;
int main(){
    int age;
    cout<<"enter your age:"<<endl;
    cin>>age;
    if (age<12)
    {
        cout<<"YOU ARE A CHILD"<<endl;
    
    }else if (age>18) {
        
        cout<<"YOU ARE AN ADULT"<<endl;
        
    }else
    {
        cout<<"you are aTEENAGER"<<endl;
        }
    
    return 0;

}