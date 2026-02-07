class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        res = len(s);
        a, b = 0, 0;

        for c in s:
            a += (c == 'a')

        for c in s:
            a -= (c == 'a');
            res = min(res, a + b);
            b += (c == 'b');

        return res;
