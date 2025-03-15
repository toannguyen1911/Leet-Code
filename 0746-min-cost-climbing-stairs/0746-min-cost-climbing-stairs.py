class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Can stand on 0 or 1
        # Each step, we can choose climb two or one step
        #  f(n): max(f(n -1), f(n -2));
        #  dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        #  Base case: 
        #  - dp[0] = cost[0]
        #  - dp[1] = cost[1]
        def dp(n):
            if (n < 0):
                return 0;
            if (n == 0 or n == 1):
                return cost[n];
            
            return cost[n] + min(dp(n -1), dp(n -2));

        top = len(cost);

        return min(dp(top -1), dp(top -2));
 
        