//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// Function to return minimum number of jumps to end of array

class Solution{
  public:
    int minJumps(int arr[], int n){
        int start=0;
        int end=0;
        int curreach=0;
        int ans=0;
        
        while(end<n-1)
        {
            for(int i=start;i<=end;i++)
            {
                curreach=max(curreach,i+arr[i]);
            }
            start=end+1;
            end=curreach;
            if(start>end) return -1;
            
            ans++;
        }
        return ans;
    }
};


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,i,j;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)
            cin>>arr[i];
        Solution obj;
        cout<<obj.minJumps(arr, n)<<endl;
    }
    return 0;
}

// } Driver Code Ends