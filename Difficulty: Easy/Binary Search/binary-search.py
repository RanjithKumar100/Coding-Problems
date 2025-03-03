#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        n = len(arr)
        low = 0
        high = n - 1
        result = -1 
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == k:
                result = mid 
                high = mid - 1 
            elif k < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    
        return result



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends