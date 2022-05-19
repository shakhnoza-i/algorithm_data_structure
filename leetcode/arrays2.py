from operator import le
from typing import List
from math import factorial


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


    def replaceElements(self, arr):
        if len(arr) <= 1:
            arr = [-1]
        elif len(arr) == 2:
            arr[-2] = arr[-1]
            arr[-1] = -1
        else:
            m = max(arr[-1], arr[-2])
            for r in range(len(arr)-2, -1, -1):
                temp = m
                m = max(m, arr[r])
                arr[r] = temp
            arr[-2] = arr[-1]
            arr[-1] = -1
        return arr


    def sortArrayByParity(self, nums):
        l = 0
        for r in range(len(nums)):
            rest = nums[r]%2
            if rest == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1       
        return nums

    
    def thirdMax(self,  nums):
        ans = 0
        x = sorted(nums)
        print(x)
        if len(nums) > 2:
            for i in range(len(x)-1, 0, -1):
                if x[i]!=x[i-1]:
                    ans+=1
                    if ans==2:
                        return x[i-1]
        return x[-1]


    def pivotIndex(self, nums):
        summ = sum(nums)
        prefix = 0

        for i, num in enumerate(nums):
            if prefix == summ - prefix - num:
                return i
            prefix += num
        return -1


    def dominantIndex(self, nums):
        if len(nums) < 2:
            return 0
        (maxValue,index) = max((value,index) for index, value in enumerate(nums))
        for i, num in enumerate(nums):
            if num <= maxValue // 2 or num == maxValue:
                continue
            else:
                return -1  
        return index

    
    def generate(self, numRows):
        outer = []
        for i in range(numRows):
            inner = []
            for j in range(i+1):
                # nCr = n!/((n-r)!*r!)
                inner.append(factorial(i)//(factorial(i-j) * (factorial(j))))
            if inner:
               outer.append(inner)
        return outer


s = Solution()

print(s.findMaxConsecutiveOnes([0,1,1,1,0,0,1,1]))
print(s.findMaxConsecutiveOnes([0,1,1,0,1,1,1,1]))
print(s.removeElement([2,3,4,4,4,0,9], 4))
print(s.replaceElements([6,8,1,5,7,2,3]))
print(s.sortArrayByParity([6,8,1,5,7,2,3]))
print(s.thirdMax([6,8,1,5,7,2,7,3]))
print(s.thirdMax([2,2,3]))
print(s.thirdMax([7,2]))
print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([2,1,-1]))
print(s.pivotIndex([1,-1,2]))
print(s.dominantIndex([3,1,6,0]))
print(s.dominantIndex([1,2,3,4]))
print(s.generate(3))
