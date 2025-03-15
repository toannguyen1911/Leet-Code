class Solution:
    def climbStairs(self, n: int) -> int:
        # Look like finaboncie
        # f(n) = f(n -1) + f(n -2)
        memory = {};
        return self.dp(n, memory);

    def dp(self, n: int, memory: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memory:
            memory[n] = self.dp(n -1, memory) + self.dp(n -2, memory)
        return memory[n];
