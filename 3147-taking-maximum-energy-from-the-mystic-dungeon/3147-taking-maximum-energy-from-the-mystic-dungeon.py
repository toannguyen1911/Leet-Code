class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [];
        n = len(energy);
        res = float('-inf');

        for i in range(n):
            step = energy[i] if i < k else max(energy[i], energy[i] + dp[i -k]);
            dp.append(step);

            if step > res and i + k >= n:
                res = step;

        return res;