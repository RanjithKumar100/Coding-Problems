//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution
{
    public:
    //Function to find the first non-repeating character in a string.
    char nonrepeatingCharacter(string S)
    {
      unordered_map<int,int> m;
      queue<char>q;
      for(auto i:S){
          ++m[i];
      if(m[i]==1){
          q.push(i);
      }
      while(q.size() && m[q.front()]>1){
          q.pop();
      }
    }
    if(q.size()){
        return q.front();
    }
    else{
        return '$';
    }
      
}
};

//{ Driver Code Starts.

int main() {
	
	int T;
	cin >> T;
	
	while(T--)
	{
	
	    string S;
	    cin >> S;
	    Solution obj;
        char ans = obj.nonrepeatingCharacter(S);
        
        if(ans != '$')
	    cout << ans;
        else cout << "-1";
            
        cout << endl;
	    
	}
	
	return 0;
}

// } Driver Code Ends