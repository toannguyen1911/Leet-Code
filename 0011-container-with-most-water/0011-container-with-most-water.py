class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Assuming container is (a, b)
        # amount of watter = (x2 - x1) * min(y1, y2)
        i, j = 0, len(height) -1;
        res = 0;

        while (i < j):
            container = j - i
            res = max(res, (j -i) * min(height[i], height[j]));
            if (height[i] <= height[j]):
                i += 1;
            else:
                j -= 1;
        
        return res;

