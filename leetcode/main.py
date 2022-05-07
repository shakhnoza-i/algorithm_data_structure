
class Solution:
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return nums


s = Solution()

print(s.removeDuplicates([1,1,2,2,2,3,4,5,5,6,6,6]))
