class Solution:
    def numSub(self, s: str) -> int:
        mod = 10 **9 + 7;
        res = 0;
        s += '0';
        cnt = 0;

        for c in s:
            if c == '1':
                cnt += 1;
                continue;
            if cnt > 0:
                res = (res + (cnt * (cnt + 1) // 2)) % mod;
                cnt = 0;
        return res;
