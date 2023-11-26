#include <iostream>
using namespace std;

int main(){

    int a,b,c;
    cout<<"enter the numbers : ";
    cin>>a>>b>>c;

    if (a>b && a>c) 
     cout<<a<<"a is the largest.";
    else if (b>c && b>a)
     cout<<b<<"b is the largest.";
    else 
     cout<<c<<"c is the largest."; 

    return 0;
}