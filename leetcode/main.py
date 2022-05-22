from operator import le
from typing import List
from collections import defaultdict
from math import factorial


class Solution:

    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return nums

    def anagrams(self, misspelled_names):
        res = defaultdict(list)
        for s in misspelled_names:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        unique = []
        for i in res.values():
            # print(i[0])
            unique.append(i[0])
        a = sorted(unique)
        return a

    def repeat(self, text, k): # HashMap solution
        words = text.split() 
        word = set([x for x in words if words.count(x) >= k])
        word = list(word)
        words = [x for x in words if x not in word ]
        
        print(words)
       

    


s = Solution()

# print(s.anagrams(["vlad", "avld", "almas", "aslam", "aya", "ayan"]))
print(s.repeat("hi ai hi ai hi", 3))