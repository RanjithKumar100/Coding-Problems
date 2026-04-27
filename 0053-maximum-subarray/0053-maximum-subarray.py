class Solution(object):
    def maxSubArray(self, nums):
        maxsub = nums[0]
        currSum = 0
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i 
            maxsub = max(maxsub,currSum)
        return maxsub