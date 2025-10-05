class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle);
        dp = [0] * n;
        num = 0;

        for i in range(n -1, 0, -1):
            row = triangle[i];
            temp = [];
            for j in range(i):
                num = min(row[j], row[j +1]) if i == n -1 else min(row[j] + dp[i][j], row[j +1] + dp[i][j +1]);
                temp.append(num);
            dp[i -1] = temp;
           
        return triangle[0][0] + num;