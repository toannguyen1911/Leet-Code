class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        Target: find the
            + The top edge of the rectangle must be at the same row as the highest 1 in the grid.
            + The bottom edge must align with the lowest 1.
            + The left edge must align with the leftmost 1.
            + ;The right edge must align with the rightmost 1.
        """
        m, n = len(grid), len(grid[0]);
        top, down, left, right = m, -1, n, -1;

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    top = min(top, i);
                    down = max(down, i);
                    left = min(left, j);
                    right = max(right, j);

        return (down - top + 1) * (right - left + 1);