#include<iostream>
using namespace std;
int main(){
    int Cp,Sp;
    cout<<"ENTER COST PRICE:"<<endl;
    cin>>Cp;

    cout<<"ENTER SELLING PRICE:"<<endl;
    cin>>Sp;
    if (Cp>Sp)
    { cout<<"YOUR LOSS IS:"<<Cp-Sp<<endl;

        /* code */
    }else if (Sp>Cp)
    { cout<<"YOUR PROFIT IS:"<<Sp-Cp<<endl;
        /* code */
    }else{
        cout<<"NO PROFIT OR LOSS"<<endl;
    }
    cout<<"THANK YOU FOR YOUR PATRONGAE";
    return 0;
}