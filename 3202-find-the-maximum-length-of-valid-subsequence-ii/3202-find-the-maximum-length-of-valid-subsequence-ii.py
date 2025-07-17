class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)];
        ans = 0;

        for num in nums:
            current_rem = num % k;

            for prev_rem in range(k):
                dp[prev_rem][current_rem] = dp[current_rem][prev_rem] + 1;
                ans = max(ans, dp[prev_rem][current_rem]);

        return ans;