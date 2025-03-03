#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1 
        s = sum(arr)
        t = (n*(n+1)) // 2
        return t-s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends