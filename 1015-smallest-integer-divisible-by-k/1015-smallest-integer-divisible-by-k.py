class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        Time complexity: O(k)
        Space complexity: O(1)
        """

        if k == 1:
            return 1;

        # Any number that ends in 1 is never divisible by 2 or 5
        if k % 2 == 0 or k % 5 == 0:
            return -1;

        # We don’t need the whole number ,we just need the remainder.
        rem = 0;

        # There are only k possible remainders
        # If we go beyond k steps, some remainder will repeat => redundant
        for i in range(1, k +1):
            rem = (rem *10 + 1) % k;
            if rem == 0:
                return i;
        return -1;
