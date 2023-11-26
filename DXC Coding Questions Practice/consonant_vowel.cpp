#include <iostream>
using namespace std;

int main(){
    char c;
    cout<<"Enter a charcter : ";
    cin>>c;

    bool upperbool,lowerbool;
    lowerbool = (c=='a' || c=='e' || c=='i' || c=='o' || c=='u');
    upperbool = (c=='A' || c=='E' || c=='I' || c=='O' || c=='U');

    if (!isalpha(c))
     cout<<"Not a charcter";
    else if (lowerbool || upperbool)
     cout<<"It is a vowel";
    else
     cout<<"It is a consonant";

    return 0;  
}