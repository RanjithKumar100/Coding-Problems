#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        l = []
        f = 0
        s = 1
        l.append(f)
        for i in range(1,n):
            l.append(s)
            t = f + s
            f = s
            s = t
        return l
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n = int(input())
        res = Solution().fibonacciNumbers(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")

# } Driver Code Ends