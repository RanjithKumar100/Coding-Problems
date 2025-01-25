#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        freq = dict()
        ans = 0
        for element in a:
            if element not in freq:
                freq[element] = 1
                ans += 1
        for element in b:
            if element not in freq:
                freq[element] = 1
                ans += 1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.findUnion(a, b))
        print("~")

# } Driver Code Ends