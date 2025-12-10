class Solution:
    def countCollisions(self, directions: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        res = 0;
        n = len(directions);
        l, r = 0, n;

        for i in range(n):
            if directions[i] != "L":
                break;
            l = i +1;

        for i in range(n -1, -1, -1):
            if directions[i] != "R":
                break;
            r = i;

        for c in directions[l: r]:
            if c != "S":
                res += 1;

        return res;