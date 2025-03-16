#include<iostream>
using namespace std;
int main(){
    int score;
    cin>>score;
    //if score>80 print WELL DONE
    //ifscore>50<80 print CAN IMPROVE
    //Otherwise print POOR PERFORMENCE

    if(score>80){
        cout<<"WELL DONE"<<endl;
    }else if (score>50)
    {cout<<"CAN IMPROVE"<<endl;
        /* code */
    }else{
        cout<<"POOR PERFORMANCE"<<endl;
    }
    return 0;
}