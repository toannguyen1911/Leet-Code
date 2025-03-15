class Solution:
    def tribonacci(self, n: int) -> int:
        #  F(N) = F(N -3) + F(N -2) + F(N -1)
        f = {};
        f[0], f[1], f[2] = 0, 1, 1;

        return self.dp(n, f);
    
    def dp(self, n: int, f: dict [int, int]) -> int:
        if n not in f:
            f[n] = self.dp(n -1, f) + self.dp(n -2, f) + self.dp(n -3, f);
        return f[n];