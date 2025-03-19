#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        index_map = {}  
        min_index = float('inf')
        for i, num in enumerate(arr):
            if num in index_map:
                min_index = min(min_index, index_map[num])
            else:
                index_map[num] = i + 1
    
        return min_index if min_index != float('inf') else -1
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr))
        print("~")

# } Driver Code Ends