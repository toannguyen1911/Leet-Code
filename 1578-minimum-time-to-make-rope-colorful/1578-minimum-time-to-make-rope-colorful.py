class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0;
        n = len(colors);
        cost = neededTime[0];
        count = 1;

        for i in range(n):
            if i == n -1:
                if count > 1:
                    res += cost;
                break;
            if (colors[i] == colors[i +1]):
                count += 1;
                if neededTime[i +1] < cost:
                    cost = neededTime[i +1];
            else:
                if count > 1:
                    res += cost;
                cost = neededTime[i +1];
                count = 1;
        
        return res;