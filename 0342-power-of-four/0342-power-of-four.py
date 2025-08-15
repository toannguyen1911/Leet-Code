class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 0;

        while (True):
            num = 4 **x;

            if (num == n):
                return True;
            if (num > n):
                return False;
            x += 1;

        return True;