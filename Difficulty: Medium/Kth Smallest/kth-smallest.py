#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        arr.sort()
        n=k-1
        p=[]
        for i in range(len(arr)):
            if i==k-1:
                p.append(arr[i])
        for i in range(len(p)):
            return p[i]
                
            
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))
        print("~")
# } Driver Code Ends