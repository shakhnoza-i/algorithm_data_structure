class Solution:

    def missingNumber(self, nums): # O(n) - time, O(1) - space complexity
        res = len(nums) # started from 9
        for i in range(len(nums)): # i range: from 0 to 8 inclusively
            res += (i - nums[i])
        return res

    def reverseBits(self, n): # O(1) - time and space complexity
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # get the first bit of n and put it in 31 spot
        # logic or, shift bit to the right by 31-i
            res = res | (bit << (31 - i))
        return res


s = Solution()

s.missingNumber([7,4,1,2,8,9,0,6,3])
