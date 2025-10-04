class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = 0;

        while i < j:
            ans = max(res, (j - i) * min(height[i], height[j]));
            if height[i] < height[j]:
                i += 1;
                continue;
            j -= 1;

        return ans;
