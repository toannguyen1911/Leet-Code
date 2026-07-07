class Solution:
    def sumAndMultiply(self, n: int) -> int:
        """
            Time complexity: O(n)
            Space complexity: O(1)
        """

        res = "";
        s = 0;

        for c in str(n):
            if c != '0':
                res += c;
                s += int(c);

        if s == 0:
            return 0;

        res = int(res) * s;

        return res;