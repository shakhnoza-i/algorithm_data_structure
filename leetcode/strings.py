import math
from collections import defaultdict

from numpy import r_

class Solution:
    
    def reverseString(self, s): # Two pointers solution
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

    def firstUniqChar(self, s): # HashMap solution
        # O(n) for time and space complexity
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
        for i in range(len(strs[0])): # take first letter of first string
            for s in strs: # s is a strings in list
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

    def lengthOfUniqueSubstring(self, s):
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:   # remove the most left character
                charSet.remove(s[l]) # until we don't have duplicates 
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1) # res - length of charSet
        return res

    def characterReplacement(self, s, k): # Sliding window technique - Two Pointers
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

    def groupAnagrams(self, strs): # O(m*n), m-number of strings, n-average length of strings
        res = defaultdict(list) # mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1 # a = 80, b = 81...-> a=80-80=0, b=81-80=1...
            res[tuple(count)].append(s) # in python lists cannot be keys, so we use tuple()
        return res.values()

    def isValidParentheses(self, s):
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in closeToOpen: # we have ")", "]", "}" in closeToOpen
            # check that the last added character corresponds to it's value
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

    def longestPalindrome(self, s):
        res = ""
        resLen = 0
        for i in range(len(s)): # take letter as mid and expand evenly on the sides
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

    def palindromeQuantity(self, s):
        res = 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1            
            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

    def reverseWords(self, s: str) -> str:
        # first split the string into words 
        words = s.split(' ') 
        # then reverse the split string list and join using space 
        words.reverse()
        reverse_sentence = ' '.join(words)
        return reverse_sentence    

    def reverseWords2(self, s: str) -> str:
        r_sentence = []
        words = s.split(' ') 
        for i in range(len(words)):
            r = list(words[i])
            r.reverse()
            r_word = ''.join(r)
            r_word = str(r_word)
            r_sentence += r_word
        return r_sentence


s = Solution()

# a = s.lengthOfUniqueSubstring("yfhdjfos")
# b = s.isValidParentheses("]([{}))")
# print(s.reverseString("the sky is blue"))
print(s.reverseWords2("the sky is blue"))
