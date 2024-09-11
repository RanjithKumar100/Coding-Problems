//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++

class Solution
{
  public:
    //Function to check if a string is Pangram or not.
    bool checkPangram (string s) {
        set<char> s1;
        for(char ch : s){
            if(ch>='a'&&ch<='z'){
                s1.insert(ch);
            }
            else if(ch>='A'&&ch<='Z'){
                ch=tolower(ch);
                s1.insert(ch);
            }
        }
        if(s1.size()==26){
            return 1;
        }
        else{
            return 0;
        }
    }

};

//{ Driver Code Starts.

// Driver Program to test above functions
int main()
{
    int t;
    cin>>t;
    cin.ignore(INT_MAX, '\n');
    while(t--){
        string s;
        getline(cin, s);
        Solution obj;
        if (obj.checkPangram(s) == true)
            cout<<1<<endl;
        else
            cout<<0<<endl;
    }
    return(0);
}

// } Driver Code Ends