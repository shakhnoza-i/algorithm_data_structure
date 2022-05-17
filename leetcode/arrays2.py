from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones +=1
                res = max(res, ones)
            else:
                ones = 0
        return res


    def findNumbers(self, nums):
        str_num = map(str, nums)
        count = 0
        for s in str_num:
            if len(s) % 2 == 0:
                count += 1
        return count
        

s = Solution()

print(s.findMaxConsecutiveOnes([0,1,1,1,0,0,1,1]))
print(s.findMaxConsecutiveOnes([0,1,1,0,1,1,1,1]))
