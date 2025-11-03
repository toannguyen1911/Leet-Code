class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0;
        n = len(colors);
        cost = neededTime[0];
        count = 1;

        for i in range(1 , n):
            if (colors[i] == colors[i -1]):
                res += min(neededTime[i], neededTime[i -1]);
                neededTime[i] = max(neededTime[i], neededTime[i -1]);
        return res;