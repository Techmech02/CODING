#include<iostream>
using namespace std;
int main(){
    int num;
    cout<<"ENTER THE NUMBER  :"<<endl;
    cin>>num;

    int c=num%2;

    if (c==0)
    { cout<<"GIVEN NUMBER IS EVEN "<<endl;
        /* code */
    }else{
        cout<<"GIVEN NUMBER IS ODD"<<endl;
    }

    return 0;

    
}