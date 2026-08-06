class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if n % 10 == 0:
            return n;

        q, r = divmod(n, 10);

        # Single digit number
        if q == 0:
            return next((x for x in range(r, 10) if x % t == 0), 10);

        for x in range(r, 10):
            if (q * x) % t == 0:
                return q * 10 + x;

        return (q + 1) * 10;