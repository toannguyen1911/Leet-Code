class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1;
        i = 0;
        n = len(num);

        while (i <= n -3):
            pre_num, cur_num, next_num = int(num[i]), int(num[i +1]), int(num[i + 2]);

            if cur_num != next_num:
                i += 2;
                continue;
            if pre_num != cur_num:
                i += 1;
                continue;
            i += 1;
            if pre_num > ans:
                ans = pre_num;

        return "" if ans < 0 else str(ans) *3;