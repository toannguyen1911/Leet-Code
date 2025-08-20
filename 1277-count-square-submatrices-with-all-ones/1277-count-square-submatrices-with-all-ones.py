class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix);
        m = len(matrix[0]);
        
        ans = 0;
        dp = [[0] * m for _ in range(n)];

        # Base case
        # Initialize first column
        for i in range(n):
            dp[i][0] = matrix[i][0];
        # Initialize first row
        for j in range(m):
            dp[0][j] = matrix[0][j];

        # Fill DP table
        # dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]).
        # dp[i][j] is the width of the biggest square

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    # submatrices [1] is square submatrices so we need + 1 
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1;
                    continue;
                # dp[i][j] = 0;

        # Count all squares
        for i in range(n):
            for j in range(m):
                ans += dp[i][j];

        return ans;