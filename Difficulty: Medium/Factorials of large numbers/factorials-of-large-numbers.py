#User function Template for python3

class Solution:
    def factorial(self, n):
        f = 1
        for i in range(1,n+1):
            f = f * i
        return [int(digit) for digit in str(f)]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N)
        print(" ".join(
            str(i) for i in
            ans))  # Join each digit to form the full number without spaces
        print("~")

# } Driver Code Ends