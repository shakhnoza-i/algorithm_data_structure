import math

class Solution:
    
    def reverseString(self, s):
        # Time - O(n), Space - O(1)
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

    def reverseInteger(self, x):
    # 32-bit integer range [-2^31, 2^31 - 1] - if go outside return 0
        MIN = -2147483648 # -2^31
        MAX = 2147483647 # 2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x/10)
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit
        return res

    def firstUniqChar(self, s): # O(n) for time and space complexity
        prevMap = {} # = index: Boolean value - {i: True} - every previous value store
        for i in range(len(s)): # i - index, True and False - value
            if s[i] not in prevMap:
                prevMap[s[i]] = True
            else:
                prevMap[s[i]] = False
        for i in range(len(s)):
            if prevMap[s[i]]:
                return i
        return -1

    def isAnagram(self, s, t): # HashMap solution
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # get s[i] value or 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c): # helper function for isPalindrome
        return (
               ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord('0') <= ord(c) <= ord('9')
               )

    def strStr(self, haystack, needle): # if needle in haystack
        if needle == "": # O(n+m) - time complexity, O(1) - space complexity
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle: #[i: j]-return values between i and j
                return i
        return -1

    def longestCommonPrefix(self, strs):
        res = "" 
        for i in range(len(strs[0])): # take first string first letter
            for s in strs: # s is a strings in list
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


s = Solution()
