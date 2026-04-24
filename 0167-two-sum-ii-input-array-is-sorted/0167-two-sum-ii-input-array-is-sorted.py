class Solution(object):
    def twoSum(self, numbers, target):
        numstoindex = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in numstoindex:
                return numstoindex[complement]+1,i+1
            numstoindex[numbers[i]] = i        