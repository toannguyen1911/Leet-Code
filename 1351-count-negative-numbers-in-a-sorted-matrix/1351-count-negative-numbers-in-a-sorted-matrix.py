class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binary_search(row):
            n = len(row)
            left, right = 0, n;
            while (left < right):
                mid = left + (right - left) // 2;

                if (row[mid] < 0):
                    right = mid;
                else:
                    left = mid + 1;
            return n - left;

        ans = 0;
        for row in grid:
            ans += binary_search(row);
        return ans;

        return 