#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        arr.sort()
        z=[]
        o=[]
        t=[]
        result=[]
        for i in range(len(arr)):
            if arr[i]==0:
                z.append(arr[i])
            elif arr[i]==1:
                o.append(arr[i])
            else:
                t.append(arr[i])
        result = z+o+t
        return result
        

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends