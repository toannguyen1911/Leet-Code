class Solution:
    def countTriples(self, n: int) -> int:
        """
            Time complexity: O(n^2);
            Space compllexity: O(1);
        """
        res = 0;
        for a in range(1, n -1):
            for b in range(a +1, n):
                c = abs(a **2 + b **2);
                if c > n:
                    break;
                res += 2;

        return res;