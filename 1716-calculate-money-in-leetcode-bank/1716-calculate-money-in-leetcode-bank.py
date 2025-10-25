class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0;
        add = 0;

        for i in range(n):
            if i % 7 == 0:
                add += 1;
            res += (i %7) + add;
        return res;