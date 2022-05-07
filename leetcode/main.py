
class Solution:

    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return nums


    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                diff = prices[i] - prices[i - 1]
                profit += diff
        return profit
    

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    def rotate_reverse(self, nums, k): # 0(1)
        k = k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums) - 1)        
        return nums


    def rotate(self, nums, k): # O(n)
        # if index >= len(nums) -> index - len(nums)
        for i in range(len(nums)):
            i = (i + k)%len(nums)

    def containsDuplicate(self, nums):
        a = set(nums)
        if len(a) == len(nums):
            return False
        else: 
            return True


s = Solution()

# print(s.removeDuplicates([1,1,2,2,2,3,4,5,5,6,6,6]))
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
print(s.rotate_reverse([7,6,4,3,1], 2))
print(s.containsDuplicate([7,6,4,3,1]))
print(s.containsDuplicate([7,6,6,3,1]))
