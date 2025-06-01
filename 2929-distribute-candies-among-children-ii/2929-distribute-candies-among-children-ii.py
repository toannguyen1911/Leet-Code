class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # x, y , n - x - y
        # child 1: 0 <= x <= limit
        # child 2: 0 <= y <= limit, x + y <= n
        # child 3: n - x - y;
        # Use binary search
        ans = 0;

        dp = [0] * (n + 1)
        dp[0] = 1; # Base case: 1 way to distribute 0 candies

        for child in range(3):
            next_dp = [0] * (n + 1);
            for i in range(n + 1): # n candies
                for j in range(min(i, limit) + 1):
                    next_dp[i] += dp[i - j];
            dp = next_dp;
                
        return dp[n];