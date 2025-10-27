class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        Time Complexity: O(m × n), where m = number of rows, n = length of each row.
        Space Complexity: O(1)
        """

        res = 0
        prev = 0

        for row in bank:
            # Count devices in the current row
            count = row.count('1')
            # Add beams between previous and current row
            if count:
                res += prev * count;
                prev = count;

        return res
