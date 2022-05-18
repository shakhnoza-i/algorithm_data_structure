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

    def removeElement(self, nums, val):
        i =0
        while i < len(nums):
            if nums[i] == val: 
                nums.remove(val) #remove by value   #del nums[-1], del nums[2:4] - remove by index
                i -= 1
            i += 1
        return nums


s = Solution()

print(s.findMaxConsecutiveOnes([0,1,1,1,0,0,1,1]))
print(s.findMaxConsecutiveOnes([0,1,1,0,1,1,1,1]))
print(s.removeElement([2,3,4,4,4,0,9], 4))
