class Solution:
    def fib(self, n: int) -> int:
        memo = {};
        return self.dp(n, memo)
        
    def dp(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return n
        if (n not in memo):
            memo[n] = self.dp(n -1, memo) + self.dp(n -2, memo);

        return memo[n];