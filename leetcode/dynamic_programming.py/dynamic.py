class Solution:


    def maxProfit(self, prices):
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # cause we find lower price 
            r += 1
        return maxP


    def climbingStairs(self, n): # similar to Fibonacchi numbers
        # dp - cashing result (memorization) for eliminate repeated work
        # dp - bottom up solution (dfs with cashing)
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


    def houseRobber(self, nums): # O(n) - time complexity
        rob1, rob2 = 0, 0
    # rob = max(arr[0]+rob[2:n], rob[1:n])
    # we need only two previous results
        # [rob1, rob2, n, n+1,...]
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    def houseRobber2(self,nums): # O(n) - time complexity
        # one element in list, list without first element, list without last element
        return max(nums[0], self.houseRobber(nums[1:]), self.houseRobber(nums[:-1]))


    def coinChange(self, coins, amount):
        # dp - bottom up solution (dfs with cashing)
        dp = [amount + 1] * (amount + 1) # 0...amount
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1


    def longestIncreasingSubsequence(self, nums): # O(n^2) - time complexity
        LIS = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

    
    def longestCommonSubsequence(self, text1, text2): # O(n*m) - time space complexity
        # dp - bottom up solution in picture(start right bottom)
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] # move diagonally
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]


    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict: # for w(word) match to this portion
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: # if dp[i] is True,
                    break # we break inner loop and go to next index
        return dp[0]


s = Solution()

print(s.houseRobber([4,7,9,3,1,6,2]))
