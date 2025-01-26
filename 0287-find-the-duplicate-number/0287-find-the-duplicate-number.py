class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p=set()
        for num in nums:
            if num in p:
                return num
            else:
                p.add(num)