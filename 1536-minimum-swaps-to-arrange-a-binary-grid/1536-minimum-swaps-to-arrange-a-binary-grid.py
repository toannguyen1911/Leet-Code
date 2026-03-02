class Solution:
    """
        Time complexity: O(n ^2)
        Space complexity: O(n)
    """
    def findMatchIdx(self, rows: list[int], zeroesNeeded: int) -> int:
        for i, zeroes in enumerate(rows):
            if zeroes >= zeroesNeeded:
                return i;
        return -1;

    def minSwaps(self, grid: List[List[int]]) -> int:
        res = 0;
        max_right = [];
        m, n = len(grid), len(grid[0]);

        # Count trailing zeroes for each row
        for i in range(m):
            count = 0;
            for j in range(n -1, -1, -1):
                if grid[i][j] == 1:
                    break;
                count += 1;
            max_right.append(count);

        # Greedy: bring suitable row upward
        for zeroes_needed in range(m -1, 0, -1):
            match_idx = self.findMatchIdx(max_right, zeroes_needed);
            if match_idx < 0:
                return -1;
            
            res += match_idx;
            max_right.pop(match_idx);

        return res;