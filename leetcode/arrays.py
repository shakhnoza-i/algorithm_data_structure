import collections
from collections import Counter

class Solution:

    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return nums


    def maxProfit2(self, prices): # multiple transactions
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

# we use bit manipulation here - XOR - return zero if two bits exact same
    def singleNumber(self, nums): # O(1) memory solution
        res = 0 # 1^0=1, 0^0=0 -if second bit is 0, result equal to first bit
        for n in nums:
            res = n ^ res
        return res

# this algorithm better for 3 case
    def intersect(self, nums1, nums2): # O(n) space and time complexity
        c = Counter(nums1)
        output = []
        for n in nums2:
            if c[n]>0:
                output.append(n)
                c[n]-=1
        return output


    def plusOne(self, digits):
        digits = digits[::-1] # reverse digits
        one, i = 1, 0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]


    def moveZeroes(self, nums): # same as removeDublicates
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


    def dublicateZeros(self, arr): 
        l = 0 # save value after 0


    def twoSum(self, nums, target): # HashMap solution
        prevMap = {} # val: index {n: i} - every previous value store
        for i, n in enumerate(nums): # i - index, n - number
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i] # first index, i - second index
            prevMap[n] = i # val: index {n: i}


    def isValidSudoku(self, board):
        cols = collections.defaultdict(set) # key - column number, value - all values in column
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": 
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c]) # update hash
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True


    def exceptSelf(self, nums):
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    def max_subarray(self, nums): # O(n)
        maxSub = nums[0]
        curSum= 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

# dynamic programming problem
    def max_product(self, nums): # O(n)
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res

    def find_min(self, nums): # Sliding window technique - Two Pointers
        # rotated sorted array
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if  nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

    def threeSum(self, nums, target):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i -1]: # if is the same value as before
                continue
        # next we use two pointers solution for the remaining portion of array
            l, r = i + 1, len(nums) -1
            while l < r:
                threeSum = a + nums[l] +nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

    def maxArea(self, height):
        # O(n) - linear time solution
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
 


s = Solution()

# print(s.removeDuplicates([1,1,2,2,2,3,4,5,5,6,6,6]))
print(s.maxProfit2([7,1,5,3,6,4]))
print(s.maxProfit2([1,2,3,4,5]))
print(s.maxProfit2([7,6,4,3,1]))
print(s.rotate_reverse([7,6,4,3,1], 2))
print(s.containsDuplicate([7,6,4,3,1]))
print(s.containsDuplicate([7,6,6,3,1]))
print(s.intersect([1,3,5,1], [3,6,1,2]))
print(s.plusOne([9,9,9,9,9]))
print(s.moveZeroes([0,0,8,2,0,0,0,5]))
print(s.twoSum([3,6,1,2], 3))
print(s.exceptSelf([1,2,3,4,5]))
print(s.max_subarray([3,-5,1,3,-6,3]))
print(s.max_product([-3,-5,-3]))
print(s.find_min([2,3,4,5,1]))

