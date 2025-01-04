#User function Template for python3

class Solution:
    def countSquares(self, n):
        i=1
        count=0
        while(i!=n):
            if(i*i<n):
                count+=1
            if(i*i>n):
                break
            i+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.countSquares(N))
        print("~")

# } Driver Code Ends