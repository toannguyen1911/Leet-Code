class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
            c == 0 => a = b = 0
            c == 1 => a or b = 1
        Time complexity: O(k) bit O(logn)
        Space complexity: O(1)
        """
        res = 0;

        while (a > 0 or b > 0 or c > 0):
            print(a, b, c)
            bit_a = a & 1;
            bit_b = b & 1;
            bit_c = c & 1;

            if bit_c == 0:
                res += bit_a + bit_b;
            elif (bit_a + bit_b == 0):
                res += 1;

            #  Shift all bits right ( // 2)
            a >>= 1;
            b >>= 1;
            c >>= 1;

        return res;