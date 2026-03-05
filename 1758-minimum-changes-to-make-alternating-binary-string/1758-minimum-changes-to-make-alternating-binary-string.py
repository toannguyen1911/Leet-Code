class Solution:
    def minOperations(self, s: str) -> int:
        c1 = 0; prev = '0';
        for ch in s:
            if ch != prev: c1 += 1;
            prev = '1' if prev == '0' else '0';

        c2 = 0; prev = '1';
        for ch in s:
            if ch != prev: c2 += 1;
            prev = '1' if prev == '0' else '0';

        return min(c1, c2);