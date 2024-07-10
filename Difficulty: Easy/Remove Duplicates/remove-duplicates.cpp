//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	
		
	string removeDups(string S) 
	{
	   string out = "";
	   int count[26] = {0};
	   int len = S.length();
	   for(int i=0;i<len;i++){
	       if(S[i]>='a'&&S[i]<='z'){
	           if(count[S[i]-'a']++ == 0){
	               out = out+S[i];
	           }
	           else if(S[i]>='A'&&S[i]<='Z'){
	               if(count[S[i]-'A']++ == 0){
	                   out = out+S[i];
	               }
	           }
	       }
	   }
	   return out;
	}
};

//{ Driver Code Starts.


int main() 
{
   	

   	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
   
   	int t;
   	cin >> t;
   	while(t--)
   	{
   		string s;
   		cin >> s;

   		
   		Solution ob;
   		cout << ob.removeDups(s) << "\n";
   		
   	}

    return 0;
}
// } Driver Code Ends