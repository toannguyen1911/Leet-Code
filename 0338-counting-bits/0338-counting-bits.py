class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Pattern:
            0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010
            => 8 (1000), 9 (1001) = x + 1(01), 10 (1010) = x + 2(10)
            11(1011) = x + 3(11)
        
        Time complexity: O(n)
        Space complexity: O(n)
        """
        dp = [0] * (n +1);
        sub = 1;

        for i in range(1, n +1):
            if sub *2 == i:
                sub = i;
            dp[i] = dp[i - sub] + 1;

        return dp;