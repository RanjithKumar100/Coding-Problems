#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    n = len(arr)
        if n == 1:  # If already at the last index, no jumps needed
            return 0
        if arr[0] == 0:  # If the first element is 0, we can't move
            return -1

        maxReach = arr[0]  # The farthest index reachable initially
        steps = arr[0]  # Steps we can still take
        jumps = 1  # First jump is made

        for i in range(1, n):
            if i == n - 1:  # If we have reached the last index
                return jumps

            maxReach = max(maxReach, i + arr[i])  # Update max reach
            steps -= 1  # Use a step

            if steps == 0:  # If no steps left, we must jump
                jumps += 1
                if i >= maxReach:  # If we can't move forward
                    return -1
                steps = maxReach - i  # Update steps for the next jump

        return -1  # If we never reach the last index


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends